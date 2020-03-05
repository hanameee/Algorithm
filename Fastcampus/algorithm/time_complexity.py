import hashlib


hash_table = list([0 for index in range(8)])

def get_key(data):
    hash_object = hashlib.sha256()
    hash_object.update(data.encode())
    hex_dig = hash_object.hexdigest()
    return int(hex_dig, 16)

def hash_function(key):
    return key % 8

def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    # 해당 주소에 데이터가 있다면
    if hash_table[hash_address] != 0:
        # 해당 주소부터 순회하며 다음 슬롯들을 탐색한다
        for index in range(hash_address, len(hash_table)):
            # 슬롯에 저장된 값이 없다면 저장
            if hash_table[index] == 0:
                hash_table[index] == [index_key, value]
                return
            # 슬롯에 저장된 데이터의 키가 현재 추가할 키와 동일하면 값만 업데이트
            elif hash_table[index][0] == index_key:
                hash_table[index][1] == value
                return
    else:
        hash_table[hash_address] = [index_key,value]

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index][0] == index_key:
                return hash_table[index][1]
            # 빈 공간이 있다는 것은 해당 data가 저장된 적이 없다는 뜻
            elif hash_table[index] == 0:
                return None
    else:
        return

save_data('aa','123')
save_data('ab','456')
save_data('ac','789')
print(read_data('aa'))
print(read_data('ab'))
print(read_data('ac'))