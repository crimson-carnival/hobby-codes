import java.util.Scanner;
public class ReduceToOne {

    private int input() {
        System.out.print("Enter the number: ");
        return new Scanner(System.in).nextInt();
    }

    private int steps(int n) {
        if(n <= 1) return 0;
        else if(n % 2 == 0) return 1 + steps(n/2);
        else return Math.min(1 + steps(n - 1), 1 + steps(n + 1));
    }

    private void output(int steps) {
        System.out.println("Minimum steps = " + steps);
    }

    public void run() {
        output(steps(input()));
    }

    public static void main(String args[]) {
        new ReduceToOne().run();
    }
}