from cmusphinx import transcript as sphinx_transcript
from wit_ai import transcript as witai_transcript
from Benchmark import Benchmark


solutions = [
    {
        'name' : 'cmusphinx',
        'transcript' : sphinx_transcript, 
    },
    {
        'name' : 'witai',
        'transcript' : witai_transcript
    }
]

speech_recognizer_benchmark = Benchmark(solutions)

result = speech_recognizer_benchmark.run()

speech_recognizer_benchmark.print()