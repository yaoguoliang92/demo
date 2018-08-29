#删除链表中的节点
#请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。
#现有一个链表 -- head = [4,5,1,9]，它可以表示为:
#   4 -> 5 -> 1 -> 9
class Solution:
	def deleteNode(self, node):
		node.val=node.next.val#当前值被后一个值覆盖
        node.next=node.next.next#下一节点跳到下下一节点
	        