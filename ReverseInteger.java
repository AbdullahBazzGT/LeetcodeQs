/**
 * Given a signed 32-bit integer x, return x with its digits reversed. If
 * reversing x causes the value to go outside the signed 32-bit integer range
 * [-231, 231 - 1], then return 0.
 * Assume the environment does not allow you to store 64-bit integers (signed or
 * unsigned).
 */

public class ReverseInteger {
    public int reverse(int x) {
        double rev = 0;
        double temp = (double) x;

        if (x < 0) {
            temp *= -1;
        }

        int len = String.valueOf(x).length();

        if (len == 1) {
            return x;
        }

        for (int i = 0; i < len; i++) {
            rev = (rev * 10) + (temp % 10);
            temp = Math.floor(temp / 10);
        }

        if (x < 0) {
            rev = -1 * (rev / 10);
        }

        if (rev > Integer.MAX_VALUE || rev < Integer.MIN_VALUE) {
            return 0;
        }

        return (int) rev;
    }
}
