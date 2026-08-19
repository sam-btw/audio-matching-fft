import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def read_audio_file(filename):
    sampling_rate, audio_signal = wavfile.read(filename)
    if audio_signal.ndim > 1:
        audio_signal = np.mean(audio_signal, axis=1)
    audio_signal = audio_signal.astype(np.float32)
    return sampling_rate, audio_signal

def calculate_fourier_magnitude(segment):
    segment = segment * np.hamming(len(segment))
    fourier_result = np.fft.rfft(segment)
    magnitude = np.abs(fourier_result)
    return magnitude

def main():
    audio_filename = "quran.wav"
    start_time_seconds = 15.0
    clip_duration_seconds = 3.0
    step_size_seconds = 0.1

    sample_rate, full_signal = read_audio_file(audio_filename)
    full_time_axis = np.arange(len(full_signal)) / sample_rate

    start_index = int(start_time_seconds * sample_rate)
    duration_in_samples = int(clip_duration_seconds * sample_rate)
    end_index = start_index + duration_in_samples

    query_clip = full_signal[start_index:end_index]
    clip_time_axis = np.arange(len(query_clip)) / sample_rate

    clip_magnitude = calculate_fourier_magnitude(query_clip)
    frequency_axis = np.fft.rfftfreq(len(query_clip), 1 / sample_rate)

    step_samples = int(step_size_seconds * sample_rate)
    window_length = len(query_clip)

    similarity_scores = []
    time_steps = []

    clip_normalization = np.linalg.norm(clip_magnitude)

    for current_index in range(0, len(full_signal) - window_length + 1, step_samples):
        current_window = full_signal[current_index:current_index + window_length]
        window_magnitude = calculate_fourier_magnitude(current_window)
        window_normalization = np.linalg.norm(window_magnitude)

        if clip_normalization == 0 or window_normalization == 0:
            similarity = 0
        else:
            similarity = np.dot(clip_magnitude, window_magnitude) / (
                clip_normalization * window_normalization
            )

        similarity_scores.append(similarity)
        time_steps.append(current_index / sample_rate)

    best_index = np.argmax(similarity_scores)
    detected_time = time_steps[best_index]
    highest_score = similarity_scores[best_index]

    detected_sample = int(detected_time * sample_rate)
    matched_signal = full_signal[detected_sample:detected_sample + window_length]

    print("Sampling frequency:", sample_rate, "Hz")
    print("Length of full signal:", len(full_signal) / sample_rate, "seconds")
    print("Clip length:", len(query_clip) / sample_rate, "seconds")
    print("Original clip position:", start_time_seconds, "seconds")
    print("Detected position:", detected_time, "seconds")
    print("Best similarity score:", highest_score)

    plt.figure(figsize=(12, 4))
    plt.plot(full_time_axis, full_signal)
    plt.title("Full Signal (Time Domain)")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.tight_layout()

    plt.figure(figsize=(10, 4))
    plt.plot(clip_time_axis, query_clip)
    plt.title("Query Clip (Time Domain)")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.tight_layout()

    plt.figure(figsize=(10, 4))
    plt.plot(frequency_axis, clip_magnitude)
    plt.title("Query Clip (Frequency Domain - FFT)")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.tight_layout()

    plt.figure(figsize=(12, 4))
    plt.plot(time_steps, similarity_scores)
    plt.axvline(detected_time, linestyle="--", label=f"Detected at {detected_time:.2f} s")
    plt.title("Similarity Score vs. Time")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Similarity Score")
    plt.legend()
    plt.tight_layout()

    plt.figure(figsize=(10, 4))
    plt.plot(clip_time_axis, query_clip, label="Original Query Clip")
    plt.plot(clip_time_axis, matched_signal, linestyle="--", label="Detected Segment")
    plt.title("Original Clip vs. Detected Segment")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.tight_layout()

    plt.show()

if __name__ == "__main__":
    main()
