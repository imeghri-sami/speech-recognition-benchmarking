import time

class Benchmark :
    def __init__(self, solutions):
        self.solutions = solutions


    def run (self, audio_file = "audios/sample1.wav"):
        
        self.benchmark_result = []
        for solution in self.solutions:
            
            start_time = time.time()
            audio_transcription = solution['transcript'](audio_file)
            end_time = time.time()

            # elapsed time
            elapsed_time = end_time - start_time

            # Word Error Rate
            
            self.benchmark_result.append({
                'transcription_result' : audio_transcription,
                'solution': solution['name'],
                'transcription_time': elapsed_time,
            })

        return self.benchmark_result

    def print (self) :
        for solution in self.benchmark_result:
            print(f"--------------- Solution : {solution['solution']} ---------------")
            print(f"Transcription time : {solution['transcription_time']}")
            print(f"Result : {solution['transcription_result']}")


                
