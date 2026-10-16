"""
Quick demonstration: Running the Video-to-Transcript Data Pipeline
"""

from pipeline import VideoTranscriptionPipeline, PipelineConfig

# 1. Initialize pipeline (100% local, self-hosted Whisper)
config = PipelineConfig(
    model_size="tiny",      # 'tiny', 'base', 'small', 'medium', 'large-v3'
    output_dir="./transcripts",
    word_timestamps=True,
)
pipeline = VideoTranscriptionPipeline(config=config)

# 2. Process video
video_file = "sample_test_video.mp4"
print(f"Transcribing {video_file}...")
result = pipeline.process(video_file)

# 3. Print results
print("\n=== TRANSCRIPTION RESULTS ===")
print("Detected Language:", result.detected_language)
print("Language Confidence:", f"{result.language_probability * 100:.1f}%")
print("Total Spoken Words:", result.total_words)
print("\nFull Transcript:\n", result.full_text)

print("\n=== TIMESTAMPS ===")
for seg in result.segments:
    print(f"[{seg.start:.2f}s -> {seg.end:.2f}s] {seg.text}")

print("\nGenerated Artifacts:")
for fmt, path in result.exported_files.items():
    print(f"  - .{fmt.upper()}: {path}")