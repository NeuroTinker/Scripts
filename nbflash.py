"""

nbflash.py

command line interface for flashing NeuroBytes firmware

"""

import click        # module for making command line interfaces
import subprocess   # module for calling make files
import os

product_directories = {
    'NeuroBytes_Interneuron',
    'NeuroBytes_Photodetector'
}

@click.command()
@click.option('--product', prompt="Select a NeuroBytes product to program")
@click.option('--interface', default='stlink')

def main(product, interface):
    """Command line interface for programming NeuroBytes"""
    click.echo('Programming %s' % product)

    if product not in product_directories:
        echo('Product not found')

    os.chdir(os.path.join('/home/neurotinker', product, 'FIRMWARE'))
    make_process = subprocess.Popen("make")


if __name__ == '__main__':
    main()




