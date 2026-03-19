from typing import Literal, Dict
from backend import Magi
from backend.magi import MagiUnit


def main():
    magi = Magi()
    magi_units: Dict[Literal['Melchior', 'Balthasar', 'Casper'], MagiUnit] = (
        magi.units
    )
    message = '3 Project Proposal Drafts, 1 is a parking meter implementation in a densely populated part of a city. 2. is about protecting local film and medial from cultural homogenization through partnership with schools for increased visibility. and 3. a city-wide digital twin dashboard tracking funding, taxes, projects, etc. Which would you go for?'
    magi_units['Casper'].add_message(
        'user',
        message,
    )
    print(f'[Casper] Sending: {message}')
    magi_units['Casper'].send_messages()


if __name__ == '__main__':
    main()
