from .util import Audio
from abc import ABC, abstractmethod
from copy import deepcopy
import numpy as np
from scipy import fft, signal
from IPython.display import display
from bokeh.plotting import figure, show
from bokeh.layouts import gridplot
from bokeh.models.mappers import LinearColorMapper
from bokeh.models.ranges import DataRange1d
from bokeh.models.tools import HoverTool
from bokeh.palettes import Viridis256
from bokeh.io import output_notebook
output_notebook()


def get_samples_and_rate(input_signal, samplerate):
    if isinstance(input_signal, TimeSignal):
        if samplerate is not None:
            print('Explicitly defined samplerate gets ignored when input is a TimeSignal', samplerate)
        samples = input_signal.samples
        samplerate = input_signal.samplerate
    elif np.ndim(input_signal) > 0:
        if samplerate is None:
            raise ValueError('The samplerate needs to be defined explicitly when input is an array or other iterable')
        samples = np.asarray(input_signal)
    else:
        raise TypeError('Only TimeSignals, Numpy arrays or other iterables are supported as input, not {}'.format(type(input_signal)))
    return samples, samplerate


def get_samples(input_signal):
    if isinstance(input_signal, TimeSignal):
        return input_signal.samples
    elif np.ndim(input_signal) > 0:
        return np.asarray(input_signal)
    else:
        raise TypeError('Only TimeSignals, Numpy arrays or other iterables are supported as input, not {}'.format(type(input_signal)))


def get_both_samples_and_rate(input_signal1, input_signal2, samplerate=None):
    samples1, samplerate1 = get_samples_and_rate(input_signal1, samplerate)
    samples2, samplerate2 = get_samples_and_rate(input_signal2, samplerate)
    if samplerate1 != samplerate2:
        raise ValueError('Both signals need to have the same samplerate')
    return samples1, samples2, samplerate1


def get_both_samples(input_signal1, input_signal2):
    samples1 = get_samples(input_signal1)
    samples2 = get_samples(input_signal2)
    if isinstance(input_signal1, TimeSignal) and isinstance(input_signal2, TimeSignal) and input_signal1.samplerate != input_signal2.samplerate:
        raise ValueError('Both signals need to have the same samplerate')
    return samples1, samples2


def same_type_as(output_samples, input_signal):
    if isinstance(input_signal, TimeSignal):
        return type(input_signal)(output_samples, input_signal.samplerate)
    else:
        return output_samples


class Signal(ABC):

    @abstractmethod
    def plot(self, **fig_args):
        pass

    def _repr_html_(self):
        return show(self.plot())

    def display(self, **fig_args):
        show(self.plot(**fig_args))

class TimeSignal(Signal):

    def __init__(self, in_data, samplerate=None):
        if isinstance(in_data, Spectrum):
            self.samples = fft.irfft(in_data.spectrum)
            self.samplerate = 2 * in_data.frequencies[-1]
        else:
            if samplerate is None:
                raise ValueError('Specify sample rate when creating TimeSignal from samples')
            self.samples = in_data
            self.samplerate = samplerate
        self.timepoints = np.arange(len(self.samples)) / self.samplerate

    def plot(self, **fig_args):
        default_args = {
            'width': 900, 'height': 300,
            'x_axis_label': 'time [s]', 'y_axis_label': 'amplitude',
            'tools': 'pan,wheel_zoom,box_zoom,zoom_in,zoom_out,save,reset',
            'active_drag': 'pan',
        }
        fig = figure(**{**default_args, **fig_args})
        fig.line(self.timepoints, self.samples, line_width=2)
        return fig


    def __add__(self, other_signal):
        if isinstance(other_signal, TimeSignal):
            if self.samplerate != other_signal.samplerate:
                raise ValueError('Cannot add signals with different sample rates')
            other_samples = other_signal.samples
        elif np.ndim(other_signal) > 0:
            other_samples = np.asarray(other_signal)
        else:
            raise TypeError('Only TimeSignals, Numpy arrays or other iterables are supported as operands, not {}'.format(type(other_signal)))
        return same_type_as(self.samples + other_samples, self)


    def filter(self, coefficients):
        if isinstance(coefficients, tuple):
            if len(coefficients) == 1:
                b, = coefficients
                a = 1
            else:
                b, a = coefficients
                filtered_samples = signal.lfilter(b, a, self.samples)
        else:
            filtered_samples = signal.lfilter(coefficients, 1, self.samples)
        return same_type_as(filtered_samples, self)


class AudioSignal(TimeSignal):

    def __init__(self, in_data, samplerate=None):
        super().__init__(in_data, samplerate)

    def play(self, normalize=False):
        return display(Audio(self.samples, rate=self.samplerate, normalize=normalize))

    def plot(self, **fig_args):
        default_args = {
            'width': 900, 'height': 300, 
            'x_axis_label': 'time [s]', 'y_axis_label': 'amplitude', 
            'y_range': (-1.09, 1.09),
            'tools': 'xpan,xwheel_zoom,box_zoom,xzoom_in,xzoom_out,save,reset', 
            'active_drag': 'xpan',
            'active_inspect': 'auto',
            'active_scroll': 'auto',
            'toolbar_location': 'above',
        }
        hover_tool = HoverTool(
            tooltips=[('time [s]', '@x{0.000}'), ('amplitude', '@y{0.000}')],
            mode='vline',
        )
        fig = figure(**{**default_args, **fig_args})
        fig.line(self.timepoints, self.samples, line_width=2)
        fig.add_tools(hover_tool)
        return fig


class Spectrum(Signal):

    def __init__(self, input, samplerate=None, num_bins=None, power=1, dB=True):
        samples, samplerate = get_samples_and_rate(input, samplerate)

        if num_bins is None:
            num_bins = len(samples)

        self.power = power
        self.dB = dB

        spectrum = fft.rfft(samples, num_bins)
        self.magnitude = np.abs(spectrum)
        self.phase = np.angle(spectrum)
        self.frequencies = np.arange(len(spectrum)) * samplerate / num_bins

        if dB:
            self.magnitude = power * 10 * np.log10(np.clip(self.magnitude, 1e-12, None))
        else:
            self.magnitude **= power


    def plot(self, **fig_args):
        default_args = {
            'width': 900, 'height': 300,
            'x_axis_label': 'frequency [Hz]', 'y_axis_label': 'amplitude',
            'tools': 'pan,wheel_zoom,box_zoom,zoom_in,zoom_out,save,reset',
            'active_drag': 'pan',
            'active_inspect': 'auto',
            'active_scroll': 'auto',
            'toolbar_location': 'above',
        }
        hover_tool = HoverTool(
            tooltips=[('frequency [Hz]', '@x{0.0}'), ['amplitude', '@y{0.000}']],
            mode='vline',
        )
        if self.power == 2:
            default_args['y_axis_label'] = 'power'
            hover_tool.tooltips[1][0] = 'power'
        if self.dB:
            default_args['y_axis_label'] += ' [dB]'
            hover_tool.tooltips[1][0] += ' [dB]'
        fig = figure(**{**default_args, **fig_args})
        fig.line(self.frequencies, self.magnitude, line_width=2)
        fig.add_tools(hover_tool)
        return fig


    def set_magnitude(self, value, start=None, end=None):
        start_idx = np.argmin(np.abs(self.frequencies - start)) if start is not None else 0
        end_idx = np.argmin(np.abs(self.frequencies - end)) if end is not None else len(self.frequencies)-1
        modified_spectrum = deepcopy(self)
        modified_spectrum.magnitude[start_idx:end_idx+1] = value
        return modified_spectrum


    def modify_magnitude(self, amount, start=None, end=None):
        start_idx = np.argmin(np.abs(self.frequencies - start)) if start is not None else 0
        end_idx = np.argmin(np.abs(self.frequencies - end)) if end is not None else len(self.frequencies)-1
        modified_spectrum = deepcopy(self)
        if self.dB:
            modified_spectrum.magnitude[start_idx:end_idx+1] = np.clip(modified_spectrum.magnitude[start_idx:end_idx+1] + amount, -120, None)

        else:
            modified_spectrum.magnitude[start_idx:end_idx+1] *= amount
        return modified_spectrum


    @property
    def spectrum(self):
        if self.dB:
            magnitude = 10 ** (self.magnitude / (10 * self.power))
        else:
            magnitude = self.magnitude ** (1/self.power)
        return magnitude * np.exp(1j*self.phase)


class PowerSpectrum(Spectrum):
    def __init__(self, input, samplerate=None, num_bins=None, dB=True):
        super().__init__(input, samplerate=samplerate, num_bins=num_bins, power=2, dB=dB)


class Spectrogram(Signal):

    def __init__(self, input_signal, frame_duration, step_duration, samplerate=None, num_bins=None, window='hann', power=1, dB=True):
        samples, samplerate = get_samples_and_rate(input_signal, samplerate)

        self.power = power
        self.dB = dB

        frame_size = round(frame_duration * samplerate)
        overlap_size = round((frame_duration-step_duration) * samplerate)

        self.frequencies, self.times, self.array = signal.stft(samples, fs=samplerate, window=window, nperseg=frame_size, noverlap=overlap_size)

        if dB:
            self.array = power * 10 * np.log10(np.clip(self.array, 1e-12, None))
        else:
            self.array **= power

    def plot(self, lowest_value=None, highest_value=None, palette=None, **fig_args):
        if not palette:
            palette = list(reversed(Viridis256))
        if not lowest_value:
            lowest_value = np.min(np.abs(self.array))
        if not highest_value:
            highest_value = np.max(np.abs(self.array))
        
        default_args = {
            'width': 900, 'height': 400, 
            'x_axis_label': 'time [s]', 'y_axis_label': 'frequency [Hz]',
            'tools': 'hover,pan,wheel_zoom,box_zoom,zoom_in,zoom_out,save,reset',
            'active_drag': 'pan',
            'active_inspect': 'auto',
            'active_scroll': 'auto',
            'toolbar_location': 'above',
            'tooltips': [('time [s]', '$x{0.000}'), ('frequency [Hz]', '$y{0.}'), ['amplitude', '@image']],
        }

        if self.power == 2:
            default_args['tooltips'][2][0] = 'power'
        if self.dB:
            default_args['tooltips'][2][0] += ' [dB]'

        fig = figure(**{**default_args, **fig_args})
        if isinstance(fig.x_range, DataRange1d):
            fig.x_range.range_padding = 0
        if isinstance(fig.y_range, DataRange1d):
            fig.y_range.range_padding = 0
        mapper = LinearColorMapper(palette=palette, low=lowest_value, high=highest_value)
        fig.image([np.abs(self.array)], x=self.times[0], y=self.frequencies[0], dw=self.times[-1], dh=self.frequencies[-1], color_mapper=mapper)
        return fig
