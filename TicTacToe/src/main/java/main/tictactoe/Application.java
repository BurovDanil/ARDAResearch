package main.tictactoe;

import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;

public class Application extends javafx.application.Application {
    @Override
    public void start(Stage stage) throws IOException {
<<<<<<< HEAD
        FXMLLoader loader = new FXMLLoader(getClass().getResource("Hello:D.fxml"));
=======
        FXMLLoader loader = new FXMLLoader(getClass().getResource("FIXME.fxml"));
>>>>>>> 5e01a981b4cf691f8bcbd6c8c33624d2f211710c
        Scene scene = new Scene(loader.load(), 500, 500);
        stage.setTitle("I was here");
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }
}
