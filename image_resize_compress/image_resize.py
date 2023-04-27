# Create date: 2023-04-26
# Create by: TW1555

from PIL import Image
import typer
import os

def read_all_file(dir_path: str):
    return [os.path.join(dir_path, f) for f in os.listdir(dir_path) if f.startswith('new') is False]

def get_output_path(whole_path):
    output_dir = os.path.dirname(whole_path)
    filename = os.path.basename(whole_path)
    filename = os.path.splitext(filename)[0]
    return output_dir, filename

def get_size(file):
    return os.path.getsize(file) / 1024
    
def resize(file, output: tuple[str], width=600):
    # resize
    im = Image.open(file)
    x, y = im.size
    height = int(y * width / x)
    im = im.resize((width, height))
    output_path = os.path.join(f'{output[0]}', f'new_{output[1]}.jpg')
    im.save(output_path)
    print('Resize done')
    return output_path

def compress(file:str, output: tuple[str], kb=150, step=10, quality=80):
    o_size = get_size(file)
    if o_size <= kb:
        print('No need to compress')
        return file, get_size(file)
    output_path = os.path.join(f'{output[0]}', f'new_{output[1]}.jpg')
    while o_size > kb:
        im = Image.open(file)
        im.save(output_path, quality=quality)
        if quality - step < 0:
            break
        quality -= step
        o_size = get_size(output_path)
    print('Compress done')
    return output_path, get_size(output_path)

def main(dir_path:str):
    
    #list all file
    print('Deal with below image now')
    print('-'*20)
    all_file = read_all_file(dir_path)
    for i in all_file:
        print(os.path.basename(i))
    print('-'*20)

    # Deal with all file in loop
    for img in all_file:
        
        print('Rearrange with {}'.format(os.path.basename(img)))

        # get output path
        output = get_output_path(img)

        # resize
        output_path = resize(img, output)

        # compress
        output_path, new_size = compress(output_path, output)
        print('New file path: {}'.format(output_path))
        print('New size: {}'.format(new_size))
        print('-'*20)

if __name__ == '__main__':
    typer.run(main)



