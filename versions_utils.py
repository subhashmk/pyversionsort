from functools import cmp_to_key

def compare_versions(version1, version2):
    lValue, rValue, length = 0, 0, 0
    version1_numbers = version1.split(".")
    version2_numbers = version2.split(".")
    len1, len2 = len(version1_numbers), len(version2_numbers)

    length = len2
    if len1 > len2:
        length = len1

    for indx in range(length):
        if indx < len1 and indx < len2:
            if version1_numbers[indx] == version2_numbers[indx]:
                continue

            lValue = 0
            if indx < len1:
                lValue = int(version1_numbers[indx])
            rValue = 0
            if indx < len2:
                rValue = int(version2_numbers[indx])

            if lValue < rValue:
                return -1
            elif lValue > rValue:
                return 1
    
    return 0

if __name__ == "__main__":
    versions = ["5.6.9", "2.3.5", "5.6.10", "4.5.8"]
    print("Versions before sorting")
    print(versions)
    versionsSorted = sorted(versions, key=cmp_to_key(compare_versions))
    print("Versions after sorting")
    print(versionsSorted)
