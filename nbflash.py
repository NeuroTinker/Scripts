"""

nbflash.py

command line interface for flashing NeuroBytes firmware

"""

import click # module for making command line interfaces

product_directories = {
    'interneuron'   :   '~/NeuroBytes_Interneuron',
    'motor'         :   '~/NeuroBytes_'
}

@click.command()
@click.option('--product', prompt="Select a NeuroBytes product to program")
@click.option('--interface', default='stlink')

def main(product, interface):
    """Command line interface for programming NeuroBytes"""
    click.echo('Programming %s' % product)

if __name__ == '__main__':
    main()




