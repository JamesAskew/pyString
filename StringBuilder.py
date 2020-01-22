
PREFIX = 'this text appears before the IP Address'
SUFFIX = 'this is after the IP Address'

outputFile = open('result.txt', 'w');

f = open('ipAddresses.txt', 'r')
ipAddresses = f.read().splitlines()

for ipAddress in ipAddresses:
    outputFile.write(f'{PREFIX} {ipAddress} {SUFFIX} {ipAddress}\n')

f.close()