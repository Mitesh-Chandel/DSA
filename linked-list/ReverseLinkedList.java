/*
 * Problem: Reverse Linked List
 * Platform: LeetCode
 * Link: https://leetcode.com/problems/reverse-linked-list/
 * Difficulty: Easy
 * Approach: Walk through the list once, reversing each node's next pointer to point to the previous node.
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */
public class ReverseLinkedList {

    private static final class ListNode {
        int value;
        ListNode next;

        ListNode(int value) {
            this.value = value;
        }
    }

    public static ListNode reverseList(ListNode head) {
        ListNode previous = null;
        ListNode current = head;

        while (current != null) {
            ListNode next = current.next;
            current.next = previous;
            previous = current;
            current = next;
        }

        return previous;
    }

    private static ListNode list(int... values) {
        ListNode head = null;
        ListNode tail = null;
        for (int value : values) {
            ListNode node = new ListNode(value);
            if (head == null) {
                head = node;
            } else {
                tail.next = node;
            }
            tail = node;
        }
        return head;
    }

    private static void printList(ListNode head) {
        ListNode current = head;
        while (current != null) {
            System.out.print(current.value);
            if (current.next != null) {
                System.out.print(" -> ");
            }
            current = current.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        printList(reverseList(list(1, 2, 3, 4, 5)));
        printList(reverseList(list(1, 2)));
        printList(reverseList(list()));
    }
}

