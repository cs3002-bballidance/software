from multiprocessing import Process
import prediction
#import write_data file

def prediction_process():
	prediction.main_loop()

def write_data_process():
	#call write data function
	pass

if __name__ == '__main__':
	Process(target=prediction_process).start()
	Process(target=write_data_process).start()
