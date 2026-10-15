# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        # 找不到節點
        if root is None:
            return None

        # key 比目前節點小，到左子樹尋找
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        # key 比目前節點大，到右子樹尋找
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        # 找到要刪除的節點
        else:
            # 沒有左子節點：用右子樹接上
            if root.left is None:
                return root.right
            
            # 沒有右子節點：用左子樹接上
            if root.right is None:
                return root.left

            # 要刪的節點有左右兩個子節點：用右子樹中最小的值來取代它 (右子樹中最小的節點，一定是一路往左走到底的節點)
            successor = root.right
            # 讓 successor 一路往左移動，直到走到沒有左子節點的節點 (沿著左側找到最小值)
            while successor.left is not None:
                successor = successor.left

            # 用中序後繼的值取代目前節點
            root.val = successor.val

            # 刪除右子樹中原本的中序後繼
            root.right = self.deleteNode(root.right, successor.val)
        
        return root