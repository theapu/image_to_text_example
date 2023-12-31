import sys, os, io
import argparse

from google.cloud import vision

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

parser = argparse.ArgumentParser(description='Process arguments.')
parser.add_argument('-i', '--input', help='Input image name')
parser.add_argument('-o', '--output', help='Output text file name')
parser.add_argument('-l', '--language', help='Input text language')
parser.add_argument('-c', '--credentials', help='Google cloud console project credentials in json format')

args = parser.parse_args()

if not (args.input or args.output):
    parser.print_help()
    sys.exit()

inputfile = args.input
outputfile = args.output
language = args.language
credentials = args.credentials

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials

client = vision.ImageAnnotatorClient()

try:
    print("Reading text from image " + inputfile)
    with io.open(inputfile, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    if not language:
        response =  client.document_text_detection(image=image)
    else:
        print("Trying to detect text in language " + language)
        response =  client.document_text_detection(image=image,image_context={"language_hints": [language]})

    doctext = response.full_text_annotation.text

    print("Writing text to " + outputfile)
    with io.open(outputfile, 'w', encoding="utf-8") as outputfilewrite:
        outputfilewrite.write(doctext)
        outputfilewrite.write("\n")

    print("Done");
except Exception as e:
    print("An error occurred")
    print(f"Error: {type(e).__name__}, Message: {str(e)}")
