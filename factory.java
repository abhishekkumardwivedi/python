
// 1. interface
public interface Communication {
  void use();
}

// 2. Implement
public class Wifi implements Communication {
  @Override
  public void use() {
    System.out.println("Wifi is selected");
  }
}

public class Bluetooth implements Communication {
  @Override
  public void use() {
    System.out.println("Bluetooth is selected");
  }
}

public class Cellular implements Communication {
  @Override
  public void use() {
    System.out.print("Cellular is selected");
  }
}

// 3. Create factory
public class CommFactory {
  public static final int wifi = 0;
  public static final int bluetooth = 1;
  public static final int cellular = 2;

  public Communication selectInterface(int comm) {
    switch (comm) {
    case wifi:
      return new Wifi();
      break;
    case bluetooth:
      return new Bluetooth();
      break;
    case cellular:
      return new Cellular();
      break;
    default:
      return NULL;
    }
  }
}

// Now let's test it.
class factory {
  public static void main(String[] args) {
    CommFactory commFactory = new CommFactory();
    Communication wifiCommunication = commFactory.selectInterface(CommFactory.Wifi);
    wifiCommunication.use();
  }
}
