# Audio Matching Using Fourier Transform (FFT)

A signal-processing project developed for the **Signals and Systems Theory (COMM 401)** course at the **German University in Cairo (GUC)**.

The project explores how frequency-domain analysis can be used to locate a short audio segment inside a longer audio recording.

---

## Project Overview

The goal of this project is to identify the position of a short audio clip within a longer audio signal.

Instead of comparing only raw time-domain samples, the system analyzes the frequency content of the signals using the **Fast Fourier Transform (FFT)**.

A sliding window moves across the full audio recording, and each candidate segment is compared with the query clip using a normalized similarity score.

The position with the highest similarity is selected as the detected location.

---

## How It Works

The matching process follows these main steps:

1. Load the full WAV audio signal.
2. Convert stereo audio to mono when necessary.
3. Extract a short query clip from the recording.
4. Apply a **Hamming window** to reduce spectral leakage.
5. Compute the FFT magnitude of the query clip.
6. Move a window across the complete recording.
7. Compute the FFT magnitude for each candidate window.
8. Calculate the normalized similarity between the query and each candidate.
9. Select the position with the highest similarity score.
10. Compare the detected segment with the original query.

---

## Signal Processing Pipeline

```text
Audio File
    ↓
Audio Preprocessing
    ↓
Query Clip Extraction
    ↓
Hamming Window
    ↓
Fast Fourier Transform (FFT)
    ↓
Frequency Magnitude
    ↓
Sliding Window Search
    ↓
Similarity Calculation
    ↓
Best Matching Position
```

---

## Results

The project successfully located the selected audio segment at its expected position.

| Parameter | Result |
|---|---:|
| Sampling Frequency | 44,100 Hz |
| Full Signal Length | 891.46 s |
| Query Clip Length | 3.00 s |
| Original Clip Position | 15.00 s |
| Detected Position | 15.00 s |
| Best Similarity Score | 1.0000 |

These results demonstrate that the FFT-based matching approach was able to identify the selected segment in the tested recording.

---

## Technologies & Libraries

- **Python**
- **NumPy**
- **SciPy**
- **Matplotlib**
- Fast Fourier Transform (FFT)
- Digital Signal Processing concepts

---

## Concepts Applied

This project provided practical experience with:

- Signals and Systems
- Time-domain signal analysis
- Frequency-domain analysis
- Fast Fourier Transform
- Audio signal processing
- Hamming windowing
- Spectral leakage reduction
- Sliding-window algorithms
- Vector normalization
- Similarity analysis
- Scientific computing with Python

---

## Project Structure

```text
audio-matching-fft/
│
├── src/
│   └── audio_matching.py
│
├── results/
│   └── project result images
│
├── report/
│   └── project report
│
└── README.md
```

---

## Source Code

The Python implementation is available in the [`src`](./src) directory.

> **Note:** The original source file was no longer available when this repository was prepared. The current implementation was reconstructed from the original project report while preserving the documented algorithm and workflow.

---

## Results & Visualizations

The [`results`](./results) directory contains visualizations produced during the original project, including:

- Full audio signal in the time domain
- Query clip in the time domain
- Query clip frequency spectrum
- Similarity score across the recording
- Comparison between the original query and detected segment

---

## Project Report

The original university project report is available in the [`report`](./report) directory.

It contains the project methodology, implementation details, experimental results, plots, and conclusions.

---

## What I Learned

This project helped me connect theoretical Signals and Systems concepts with a practical engineering application.

In particular, I gained experience with:

- Applying Fourier analysis to real audio data
- Understanding the relationship between time and frequency domains
- Using FFT for practical signal analysis
- Processing WAV audio using Python
- Implementing a sliding-window search
- Comparing signals using normalized similarity
- Visualizing and interpreting signal-processing results

---

## Academic Context

**Course:** COMM 401 — Signals and Systems Theory  
**University:** German University in Cairo (GUC)

This repository documents the implementation, results, and report associated with the university project.

---

## Author

**Sama Ismael**  
Information Engineering & Technology  
German University in Cairo
