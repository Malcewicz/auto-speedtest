#! python3
import speedtest, csv, time
from datetime import datetime

NUMBER_OF_TESTS = input("Numer of tests: ")
TIME_BETWEEN_TESTS = input("Time between tests (in minutes): ")

with open('speedtestResults.csv', 'a') as csv_file:
    for test_count in range(int(NUMBER_OF_TESTS)):
        print(f'Running Test No.{test_count + 1}')
        line_writer = csv.writer(csv_file)

        threads = None
        s = speedtest.Speedtest()
        s.get_best_server()
        s.download(threads=threads)
        s.upload(threads=threads)

        line_writer.writerow([datetime.now().strftime("%d-%m-%Y %H:%M:%S"), str(s.results.share().replace(".png", " "))])
        print(f'Test No.{test_count + 1} done')
        time.sleep(int(TIME_BETWEEN_TESTS)*60)
    print('\n All tests done, writing to file speedtestResults.csv')