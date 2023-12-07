package main.tictactoe;

import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;

public class Application extends javafx.application.Application {
    @Override
    public void start(Stage stage) throws IOException {
<<<<<<< HEAD
        FXMLLoader loader = new FXMLLoader(getClass().getResource("FIXME.fxml"));
        Scene scene = new Scene(loader.load(), 500, 500);
        stage.setTitle("FIXME");
=======
        FXMLLoader loader = new FXMLLoader(getClass().getResource("HelloTher".fxml));
        Scene scene = new Scene(loader.load(), 100, 100);
        stage.setTitle("TicTacToe!");
        stage.setScene(scene);
        stage.show();
>>>>>>> parent of 60d10af (Revert "submit 3")
    }

    public static void main(String[] args) {
        launch();
    }
}
