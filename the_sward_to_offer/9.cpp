//用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
class Solution
{
public:
    void push(int node) {
        stack1.push(node);
    }

    int pop() {
        if (stack2.empty()) {
            while (!stack1.empty()) {
                int d = stack1.top();
                stack1.pop();
                stack2.push(d);
            }
        }
        int d = stack2.top();
        stack2.pop();
        return d;
    }

private:
    stack<int> stack1;
    stack<int> stack2;
};