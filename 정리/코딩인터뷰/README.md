#### 3-2 스택 Min: 기본적인 push와 pop 기능이 구현된 스택에서 최솟값을 반환하는 min함수를 추가하려고 한다. 어떻게 설계할 수 있겠는가?

---



1. Stack 클래스의 멤버로 int minValue를 둔다. minValue가 스택에서 제거되면 스택을 뒤져 새로운 최솟값을 찾는다.
   1. Push될 때마다 최소값을 계산한다.
   2. Pop을 할때는 최소값과 같은 value가 빠지면 최솟값을 계산한다.

```java
public class MinValueStack {
  public static void main(String[] args) {
    Stack stack = new Stack(2);

    stack.push(1);
    stack.push(3);
    System.out.println(stack.pop());
    System.out.println(stack.pop());

  }
}

class Stack {
  int top;
  int size;
  int[] stack;
  int minValue = Integer.MAX_VALUE;

  public Stack(int size) {
    this.size = size;
    stack = new int[size];
    top = -1;
  }

  public void push(int value) {

    int index = ++top;
    if(index >= size) {
      System.out.println("Stack Overflow");
      System.exit(-1);
    }

    minValue = Math.min(minValue, value);
    stack[index] = value;
  }

  public int pop() {

    if(this.isEmpty()) {
      System.out.println("Stack Underflow");
      System.exit(-1);
    }

    int value = stack[top];

    if(minValue == value) {
      minValue = Math.min(minValue, value);
    }

    stack[top--] = -1;
    return value;
  }

  public boolean isEmpty() {
    return top == -1;
  }
}

```


---

2. 스택의 각 상태마다 최솟값을 함께 기록한다.