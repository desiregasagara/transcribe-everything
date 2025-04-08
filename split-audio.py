from pydub import AudioSegment

song = AudioSegment.from_mp3("audios/grandparents-advice.mp3")

# PyDub handles time in milliseconds
three_minutes = 3.5 * 60 * 1000

first_3_minutes = song[:three_minutes]

first_3_minutes.export("3-min-grandparents-advice.mp3", format="mp3")