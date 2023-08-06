from collections import defaultdict, deque


class GlobalDataWareHouse(object):
    def __init__(self):
        self.DataWareHouseData = defaultdict(lambda: 'defaultvalue')
        self.DataWareHouseName = deque()

    def create(self, datawarehousename, data=None):
        self.DataWareHouseName.append(datawarehousename)
        if data is None:
            self.DataWareHouseData[datawarehousename] = {}
        else:
            self.DataWareHouseData[datawarehousename] = data

    def select(self, datawarehousename, key=None):
        if datawarehousename in self.DataWareHouseName:
            if key is None:
                return self.DataWareHouseData[datawarehousename]
            else:
                return self.DataWareHouseData[datawarehousename][key]
        return None

    def upadte(self, datawarehousename, data: dict):
        if datawarehousename in self.DataWareHouseName:
            self.DataWareHouseData[datawarehousename].update(data)
            return True
        return False

    def delete(self, datawarehousename, key):
        if datawarehousename in self.DataWareHouseName:
            self.DataWareHouseData[datawarehousename].pop(key)
            return True
        return False

    def clear(self, datawarehousename):
        if datawarehousename in self.DataWareHouseName:
            self.DataWareHouseData[datawarehousename].clear()
            return True
        return False

    def clear_all(self):
        self.DataWareHouseData.clear()
        self.DataWareHouseName.clear()
