# image_to_text_example
## Example for google vision API image to text
1. Create a project for using cloud vision api and credentials in https://console.cloud.google.com/
2. Create a python virtual environment
```
sudo apt install python3-venv
python3 -m venv home_vsion_api
cd home_vsion_api
source bin/activate
```
3. Install google-cloud-vision module
```
pip install --upgrade google-cloud-vision
```
4. Copy project credentials json from console.cloud.google.com to credentials folder
5. Run using
```
python home_vision_api_text.py -i <input image file> -o <output txt file> -l <image text language code>
```
6. To build standalinone binary install pyinstaller and build binary
```
pip install pyinstaller
pyinstaller --clean -y -F --add-data "<path to credential json>:credentials" home_vision_api_text.py
```
