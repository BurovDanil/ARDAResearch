package main.tictactoe;

import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;

public class Application extends javafx.application.Application {
    @Override
    public void start(Stage stage) throws IOException {
<<<<<<< HEAD
=======
<<<<<<< HEAD
        FXMLLoader loader = new FXMLLoader(getClass().getResource("HelloThere".fxml"));
=======
>>>>>>> parent of f6ae692 (changeApp)
        FXMLLoader loader = new FXMLLoader(getClass().getResource("HelloThere.fxml"));
        Scene scene = new Scene(loader.load(), 100, 100);
        stage.setTitle("TicTacToe!");
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }
}
