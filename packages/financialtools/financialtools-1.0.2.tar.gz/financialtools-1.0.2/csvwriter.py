import csv

def csvwriter(output,df,*args):
    filename = output
        # writing to csv file
    with open(filename, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields
        csvwriter.writerow(df.columns)

        # writing the data rows
        csvwriter.writerows(df.values)
        csvwriter.writerow([])
        csvwriter.writerow([])
        csvwriter.writerow([])
        for arg in args:
            csvwriter.writerow([arg])
