



    static Scanner cmd = new Scanner(System.in);
    static byte B = cmd.nextByte();
    static byte H = cmd.nextByte();

    static boolean flag = false;
    static{
        if (B < 1 || H < 1){
            System.out.println("java.lang.Exception: Breadth and height must be positive");
        }
        else{
            flag = true;
        }
    }




