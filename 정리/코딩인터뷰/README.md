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
> 위에 있는 방식으로 하였을때의 문제는 Push되거나 Pop이 될때 연산을 돌아야 한다는 점이다. 
> 스택의 각 상타매다 최솟값을 함께 기록한다면 스택의 최상위 노드만을 보고 최솟값을 알아낼 수 있다.
> <br/><br/>
> 이 방법도 좋아보이지만 한가지 문제가 있다. 스택이 커지면, 각 원소마다 min을 기록하느라 공간이 낭비된다.
> 그렇다면 더 나은방법은 뭐가있을까.
> <br/><br/>
> 
> 스택을 하나 더 생성해서 최소값을 저장하는 스택을 만드는 방법이 있다.

```java

public class MinValueInStack {
  public static void main(String[] args) {
    Stack stack = new Stack(10);
    stack.push(8);
    stack.push(3);
    stack.push(6);
    stack.push(2);
    stack.push(1);

    Arrays.stream(stack.stack)
      .forEach(System.out::println);

    System.out.println("-----");
    stack.pop();
    stack.pop();
    Arrays.stream(stack.stack)
      .forEach(System.out::println);
  }
}

class Stack {
  int top;
  int size;
  Element[] stack;

  public Stack(int size) {
    this.size = size;
    stack = new Element[size];
    top = -1;
  }

  public void push(int value) {

    int index = ++top;
    if(index >= size) {
      System.out.println("Stack Overflow");
      System.exit(-1);
    }

    stack[index] = new Element(value, Math.min(value, min()));
  }

  public Element pop() {

    if(this.isEmpty()) {
      System.out.println("Stack Underflow");
      System.exit(-1);
    }

    Element value = stack[top];
    stack[top--] = null;
    return value;
  }

  public Element peek() {

    int index = top;
    return this.stack[--index];
  }

  public int min() {
    if(isEmpty()) {
      return Integer.MAX_VALUE;
    }

    return peek().getMinValue();
  }

  public boolean isEmpty() {
    return Objects.isNull(stack[0]);
  }
}

class Element {
   private int value;
   private int minValue;

   public Element(int value, int minValue) {
      this.value = value;
      this.minValue = minValue;
   }

   public int getMinValue() {
      return this.minValue;
   }

   @Override
   public String toString() {
      return "Element{" +
              "value=" + value +
              ", minValue=" + minValue +
              '}';
   }
}

```

-----------------------------

#### 4-2 최소트리: 오름차순으로 정렬된 배열이 있다. 이 배열안에 들어있는 원소는 정수이며 중복된 값이 없다고 했을 때 높이가 최소가 되는 이진 탐색 트리를 만들어라.

> 이진탐색트리는 루트노드를 기준으로 작은값은 왼쪽, 큰값은 오른쪽으로 정렬되야하는 특성이 있다.
> <br><br>
> 즉 높이가 최소가 되려면 양쪽노드에 갯수를 가능하면 맞춰야한다는 말이되고, 루트를 중앙으로 두고 절반은 루트보다 작고, 너머지 절반은 루트보다 커야한다.
> 

이를 간단하게 구현하고자 한다면 다음과 같이 구현할 수 있습니다.
 - 배열의 각 중앙값은 루트가 될 것이고, 루트의 왼쪽과 오른쪽은 각각 하위트리가 된다.
 - 재귀방식을 사용한다.


첫번째 간단히 구현하는 방식으로는 루트부터 재귀를 돌면서 값을 트리에 삽입하는 방식이 있다. 이렇게하면 결국 최소높이 트리를 만들 수 있겠지만 효율적이지는 않다, 
왜냐하면 원소를 삽입할 때마다 트리를 순회해야 하므로 전체비용이 O(NlogN)이 되기 때문이다.

다른 방법으로는 배열의 일부가 주어졌을때 해당 배열로 만들 수 있는 최소높이 트리의 루트노드를 반환하는 방식이있다.

1. 배열 가운데 원소를 트리에 삽입한다.
2. 왼쪽 하위 트리에 왼쪽 절반 배열 원소들을 삽입한다.
3. 오른쪽 하위 트리에 오른쪽 절반 배열 원소들을 삽입한다.
4. 재귀 호출을 실행한다.

```java
TreeNode createMinimalBST(int[] arr) {
  return createMininalBst(arr, 0 , arr.length -1);  
}

TreeNode createMinimalBST(int[] arr, int start, int end) {
  if (end < start) {  
    return null;
  }

  int mid = (start + end) / 2;
  TreeNode n = new TreeNode(arr[mid]);
  n.left = createMinimalBST(arr, start, mid - 1);
  n.right = createMinimalBST(arr, mid + 1, end);

  return n;
}

```


 