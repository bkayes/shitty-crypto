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
    int len = nextSquare(message.length());
    rowCol(message, len);
  }
  
  public char[][] getCurrentContent(){
    return content;
  }
  
  public void updateContent(int opIndex, int numInput){
    switch(opIndex){
      case 10: rowCol(/*not sure why this is being called again?*/); break;
      case 0: nRotate(numInput); break;
      case 1: reverseRows(); break;
      case 2: caesar(numInput); break;
      case 3: cycle(numInput); break;
      case 4: shiftChars(numInput); break;
    }
  }
  
  private int nextSquare(int n){
    /* Finds the next integer which, when squared, is greater than n. */
    return (int)(Math.ceil(Math.sqrt(n)));
  }
  
  private String pad(String s, int n){
    /* Pad a given text with spaces so it's length is a multiple of n. */
    int pad_n = n - s.length() % n;
    if (pad_n == n) return s;
    String pad = new String(new char[pad_n]).replace("\0", " ");
    return s + pad;
  }

  private String[] chunk(String s, int n){
    /* Chunk text into list of char lists with size n. */
    s = pad(s,n);
    return s.split("(?<=\\G.{"+n+"})");
  }

  private void rowCol(String s, int n){
    /* Return a square list with n rows and cols of chunks of text. */
    String pad_str = new String(new char[n]).replace("\0", " ");
    String[] chunks = chunk(s, n);
    String[] padding = new String[n-chunks.length];
    for (int i = 0; i < padding.length; i++) {
      padding[i] = pad_str;
    }
    String[] square = new String[chunks.length + padding.length];
    for (int i = 0; i < square.length; i++) {
      if (i < chunks.length) {
        square[i]=chunks[i];
      } else {
        square[i]=padding[i - chunks.length];
      }
    }

    char[][] ret = new char[n][n];
    for(int i=0; i < square.length; i++){
        ret[i] = square[i].toCharArray();
    }
    content = ret;
  }
  
  private char[][] rotateOnce(char[][] square){
    int M = square.length;
    int N = square[0].length;
    char[][] ret = new char[N][M];
    for (int r = 0; r < M; r++) {
        for (int c = 0; c < N; c++) {
            ret[c][M-1-r] = square[r][c];
        }
    }
    return ret;
  }
  private void nRotate(int n){
    char[][] square = content;
    /* Given a square char array, rotate it clockwise by n turns. */
    for (int i=0; i<n; i++) {
        square = rotateOnce(square);
    }
    content = square;
  }
  
  private void reverseRows(){
    char[][] square = content;
    /* Reverse the rows of the square. */
    for(int i = 0; i < square.length / 2; i++) {
        char[] temp = square[i];
        square[i] = square[square.length - i - 1];
        square[square.length - i - 1] = temp;
    }
    content = square;
  }
  
  private void caesar(int n){
    char[][] square = content;
    /*Caesar shift all letters in the square*/
    int len = square.length;
    char[][] res = new char[len][len];
    char ch;
    for (int r = 0; r < len; r++){
        char[] row = new char[len];
        for (int c = 0; c < len; c++){
            ch = square[r][c];
            // if c is letter ONLY then shift them, else directly add it
            if (Character.isLetter(ch)){
                ch = (char) (square[r][c] + n);
                // checking case or range check is important, just if (c > 'z'
                // || c > 'Z')
                // will not work
                if ((Character.isLowerCase(square[r][c]) && ch > 'z') ||
                    (Character.isUpperCase(square[r][c]) && ch > 'Z')){
                    ch = (char) (square[r][c] - (26 - n));
                }
            }
            row[c] = ch;
        }
        res[r] = row;
    }
    content = res;
  }
  
  private void cycle(int n){
    char[][] square = content;
    int len = square.length;
    /* Cycles the character order of each row. */
    for (int r = 0; r < square.length; r++) {
      char[] row = square[r];
      for (int c = 0; c < row.length; c++) {
        row[c] = square[r][(c + n) % row.length];
      }
      square[r] = row;
    }
    content = square;
  }
  
  private void shiftChars(int n){
    char[][] square = content;
    /* Shift each character Caesar cipher style by value n */
    int len = square.length;
    char[][] res = new char[len][len];
    char ch;
    for (int r = 0; r < len; r++){
        char[] row = new char[len];
        for (int c = 0; c < len; c++){
            ch = square[r][c];
            ch = (char) ((square[r][c] + n) % 127);
            row[c] = ch;
        }
        res[r] = row;
    }
    content = res;
  }
}