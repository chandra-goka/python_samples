import string
import re
if __name__ == '__main__':
    data = '#(Hello! I need to remove $pl @hars in Pyth@n)'
    cleaned_data = data.translate(str.maketrans('','',string.punctuation))
    print(cleaned_data)
    data = '#(Hello! I need to remove $pl @hars in Pyth@n)'
    # using re
    cleaned_data = re.sub('[^A-Za-z0-9 ]+', '', data)
    print(cleaned_data)