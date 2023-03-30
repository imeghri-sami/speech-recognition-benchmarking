from cmusphinx import transcript
from Benchmark import Benchmark


solutions = [
    {
        'name' : 'cmusphinx',
        'transcript' : transcript, 
    }
]

speech_recognizer_benchmark = Benchmark(solutions)

result = speech_recognizer_benchmark.run()

print(result)