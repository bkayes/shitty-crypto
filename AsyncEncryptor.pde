/*

An object of this class encrypts a message operation by operation, one operation per iteration.
  (Depends on the length of the operation tree.)

It has an active and inactive state, governed externally.

It performs its functions when the updateContent() method is called, with the current operation specified.

Ideally, there should only ever be one of these instantiated at a time.

Therefore, an object of this class will be a member of the OperationTree object.

OPERATION CODES:
  10 -- ROWCOL
  0  -- ROTATE
  1  -- REVERSE
  2  -- CAESAR
  3  -- CYCLE
  4  -- SHIFT CHARS
  5  -- <RESERVED>
  6  -- <RESERVED>
  7  -- <RESERVED>
  8  -- <FREE>
  9  -- <FREE>
  11+ - <FREE>

*/

public class AsyncEncryptor{
 
  private char[][] content;
  
  public AsyncEncryptor(String message){
    content = rowCol(message);
  }
  
  public char[][] getCurrentContent(){
    return content;
  }
  
  public void updateContent(int opIndex, int numInput){
    switch(opIndex){
      case 10: rowCol(); break;
      case 0: nRotate(numInput); break;
      case 1: reverseRows(); break;
      case 2: caesar(numInput); break;
      case 3: cycle(numInput); break;
      case 4: shiftChars(numInput); break;
    }
  }
  
  private int nextSquare(int n){
    /* Finds the next integer which, when squared, is greater than n. */
    return Math.ceil(Math.sqrt(n));
  }
  
  private String pad(String s, int n){
    /* Pad a given text with spaces so it's length is a multiple of n. */
    int pad_n = n - s.length % n;
    if pad_n == n return s;
    string pad = new String(new char[pad_n]).replace("\0", " ");
    return s + pad;
  }

  private String[] chunk(String s, int n){
    /* Chunk text into list of char lists with size n. */
    s = pad(s,n);
    return java.util.Arrays.toString(s.split("(?<=\\G.{3})"))
  }

  private char[][] rowCol(String s, int n){
    /* Return a square list with n rows and cols of chunks of text. */
    String pad_str = new String(new char[n]).replace("\0", " ");
    String[] padding = new String[n];
    Arrays.fill(padding, pad_str);
    String[] chunks = chunk(s);
    String[] square = Stream.concat(Arrays.stream(chunks), Arrays.stream(padding)).toArray(String[]::new);

    char[][] ret = new char[n][n];
    for(int i=0; i < square.length; i++){
        ret[i] = square[i].toCharArray();
    }
    return ret;
  }
  
  private char[][] rotateOnce(char[][] square){
    int M = square.length;
    int N = square[0].length;
    int[][] ret = new int[N][M];
    for (int r = 0; r < M; r++) {
        for (int c = 0; c < N; c++) {
            ret[c][M-1-r] = square[r][c];
        }
    }
    return ret;
  }
  private char[][] nRotate(char[][] square, int n){
    /* Given a square char array, rotate it clockwise by n turns. */
    for (int i=0; i<n; i++) {
        square = rotateOnce(square);
    }
    return square;
  }
  
  private char[][] reverseRows(char[][] square){
    /* Reverse the rows of the square. */
    for(int i = 0; i < square.length / 2; i++) {
        char[] temp = square[i];
        square[i] = square[square.length - i - 1];
        square[square.length - i - 1] = temp;
    }
    return square;
  }
  
  private char[][] caesar(char[][] square, int n){
    /*Caesar shift all letters in the square*/
    len = square.length
    char[][] res = new char[len][len];
    char c;
    for (int r = 0; r < len; r++){
        row = new char[len];
        for (int c = 0; c < len){
            ch = square[r][c];
            // if c is letter ONLY then shift them, else directly add it
            if (Character.isLetter(ch)){
                ch = (char) (square[r][c] + shift);
                // checking case or range check is important, just if (c > 'z'
                // || c > 'Z')
                // will not work
                if ((Character.isLowerCase(square[r][c]) && ch > 'z') ||
                    (Character.isUpperCase(square[r][c]) && ch > 'Z')){
                    ch = (char) (square[r][c] - (26 - shift));
                }
            }
            row[c] = ch;
        }
        res[r] = row;
    }
    return res;
  }
  
  private char[][] cycle(char[][] square, int n){
    int len = square.length
    /* Cycles the character order of each row. */
    for (int r = 0; r < len; r++) {
        String row = Arrays.toString(square[r]);

    }
  }
  
  private char[][] shiftChars(char[][] square, int n){
    /* Shift each character Caesar cipher style by value n */
    
  }
}