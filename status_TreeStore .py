class TreeStore:
    def __init__(self, items):
        self.items = items

    def getAll(self):                                                 # Ничего сложного, просто возвращаем массив.
        return self.items

    def makeTree(self):                                               #  Для минимизации количества обходов, в тех методах, где необходимо выстроить путь,
        result = {}                                                   #  построим одномерный массив в виде дерева, с указателями на предков и детей каждого элемента.
        for item in self.items:
            result[item["id"]] = {}
            result[item["id"]]["object"] = item
            result[item["id"]]["parent"] = item["parent"]
            result[item["id"]]["childs"] = set()
            if item["parent"] not in result:
                result[item["parent"]] = {}
                result[item["parent"]]["childs"] = {item["id"]}
            else:
                result[item["parent"]]["childs"].add(item["id"])
        return result

    def getItem(self, id):                                            # Для ускорения поиска элемента в массиве, воспользуемся алгоритмом бинарного поиска.
        center = self.items[len(self.items) // 2]                     # В случае, когда нам необходимо найти единственный элемент, это будет быстрее, чем выстраивать массив методом makeTree и доставать данные из него.
        if center["id"] == id:
            return center
        left = self.items[:len(self.items) // 2]                      # Воздержимся от использования метода index(), для определения границ срезов левой и правой сторон.
        right = self.items[len(self.items) // 2 + 1:]
        if center["id"] < id:
            return TreeStore(right).getItem(id)
        else:
            return TreeStore(left).getItem(id)


    def getChildren(self, id):                                          # Для поиска детей заданного объекта, воспользуемся методом makeTree, созданным ранее
        result = list()                                                 # это позволит нам получить указатели на детей.
        tree = self.makeTree()
        for i in tree[id]["childs"]:
            result.append(tree[i]["object"])
        return result
    

    def getAllParents(self, id):                                      
        result = list()
        while id != "root":
            result.append(self.getItem(id))                            # Для поиска родителя по его id, воспользуемся написанным ранее методом getItem.
            id = result[-1]["parent"]                                  # Получаем id родителя. Можно было воспользоваться методом makeTree, т.к. он позволит нам получить удобные указатели на детей,
        return result                                                  # Однако использование бинарного поиска будет предпочтительнее создания дерева полным обходом.




items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]

ts = TreeStore(items)