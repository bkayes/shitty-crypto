// This is the 2d char array we're saving filled with some example chars. Change the name where applicable. 
char[][] change_me = new char[][]{{'a','b'},{'c','d'}};

// We then create a JSONArray called json to hold the object we'll be saving to a file. 
JSONArray json = new JSONArray();

for (int r = 0; r < change_me.length; r++) {
    JSONArray row = new JSONArray();
    for (int c = 0; c < change_me[0].length; c++) {
        // JSON supports string arrays, not char arrays, and python treats chars as one character strings. Cast to string by concatenating the char with an empty string. 
        String s = "" + change_me[r][c];
        row.setString(c, s);
    }
    json.setJSONArray(r, row);
}

saveJSONArray(json, "ciphertext.json");