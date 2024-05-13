from src.speech_recognition import transcribe_audio
from src.nlp_summarization import generate_summary
from src.tweet_generation import post_tweet, generate_tweet
def process_twitter_spaces(space_id):
    audio_file = f'audio/audio{space_id}.wav'
    text = transcribe_audio(audio_file)
    summary = generate_summary(text)
    tweet_text = generate_tweet(summary)
    post_tweet(tweet_text)
if __name__ == "__main__":
    space_id = 1 
    process_twitter_spaces(space_id)