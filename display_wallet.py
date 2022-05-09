import transaction
import wallet


def display_wallet():
    display = True
    while display:
        print('\n\n     Wallet'
              '\n---------------------------------'
              '\n---------------------------------')
        print('\nOptions'
              '\n1. Create key and address (compressed)'
              '\n2. Create key and address (uncompressed)'
              '\n3. Send BTC'
              '\n4. Quit')
        option = input('Choose: ')

        if option == '1':
            try:
                privKey = wallet.get_privKey()
                wif = wallet.get_wif(wallet.get_hex(privKey))
                Point = wallet.get_pubKey(privKey)
                pubKey_compressed = wallet.get_pubKey_compressed(Point)
                bitcoinAddress_compressed = wallet.get_adress(pubKey_compressed)
                print('\nPriv key: ', privKey,
                      '\nPriv key wif: ', wif,
                      '\nPub key (compressed): ', pubKey_compressed,
                      '\nAddress (compressed): ', bitcoinAddress_compressed)
            except:
                print('Cannot create compressed key and address. Please try again.')

        elif option == '2':
            try:
                privKey = wallet.get_privKey()
                Point = wallet.get_pubKey(privKey)
                pubKey_uncompressed = wallet.get_pubKey_uncompressed(Point)
                bitcoinAddress_uncompressed = wallet.get_adress(pubKey_uncompressed)
                print('\nPriv key: ', privKey,
                      '\nPub key (uncompressed): ', pubKey_uncompressed,
                      '\nAddress (uncompressed): ', bitcoinAddress_uncompressed)
            except:
                print('Cannot create uncompressed key and address. Please try again.')

        elif option == '3':
            to_address = input('Address to send to: ')
            amount = float(input('Amount to send: '))
            txid_input = input('Tx id for input: ')
            output_nr = int(input('Output number in that transaction: '))
            privKey = [input('Priv key in wif: ')]
            try:
                tx_to_sign = transaction.create(txid_input, output_nr, to_address, amount)
                signedhex = transaction.sign(tx_to_sign, privKey)
                tx_hash = transaction.send(signedhex)
                print('Transaction ', tx_hash, ' has been sent.')
            except:
                print('Cannot make transaction')

        elif option == '4':
            display = False
            print('Wallet quitting..')

        else:
            print('Please try again.')


if __name__ == "__main__":
    display_wallet()
