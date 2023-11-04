def convertToWave(arr):
    waveArray = sorted(arr)

    index = 0
    while index < len(arr) - 1:
        waveArray[index], waveArray[index + 1] = waveArray[index + 1], waveArray[index]

        index += 2

    print(waveArray)
    return waveArray

convertToWave([2,4,7,8,9,10])