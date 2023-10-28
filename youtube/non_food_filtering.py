import pandas as pd
import csv

def main():
    category = ["pasta", "burger", "pizza", "sushi", "chicken"]

    for i in range(len(category)):    
        csv_file_path = '/root/youtube/result_csv/yolo_csv/yolo_' + category[i] + '.csv' # 리스트로 사용할 csv 파일 선택

        with open(csv_file_path, 'r', newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            data = list(csv_reader)
        
        new_data_list = []
        for row in data:
            new_data = [row[0]]
            contents = row[1:]
            for j in range(len(contents)):
                data = contents[j].replace('"', '')
                res_data = data.split(',')

                frame_len = float(res_data[5])
                food_count = float(res_data[6])
                
                if (frame_len > 0):
                    if (food_count / frame_len) > 0.15 :
                        new_data.append(','.join(res_data))
            new_data_list.append(new_data)

            yolo_file_path = '/root/youtube/result_csv/filter_csv/yolo_filter_' + category[i] + '.csv' # 리스트로 사용할 csv 파일 선택
            with open(yolo_file_path, 'w', newline='', encoding='utf-8') as csv_file:
                csv_writer = csv.writer(csv_file)
                for data_list in new_data_list:
                    csv_writer.writerow(data_list)
            
            
          
if __name__ == '__main__':
    main()