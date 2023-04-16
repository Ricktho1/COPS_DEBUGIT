import 'package:flutter/material.dart';
import 'package:to_do_list/todo.dart';
import 'dialog_box.dart';

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  final _taskController = TextEditingController();

  List ToDoList = [
    ["Coding", false],
    ["Attend Club activities", false],
    ["Dance", false],
  ];

  void saveNewTask() {
    setState(
      () {
        ToDoList.add([_taskController.text, false]);
        _taskController.clear();
      },
    );
  }

  void deleteTask(int index) {
    setState(() {
      ToDoList.removeAt(index);
    });
  }

  void createNewTask() {
    showDialog(
      context: context,
      builder: (context) {
        return DialogBox(
          Controller: _taskController,
          onSave: saveNewTask,
        );
      },
    );
  }

  void checkBoxChanged(bool? value, int index) {
    setState(() {
      ToDoList[index][1] = !ToDoList[index][1];
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Theme.of(context).backgroundColor,
      appBar: AppBar(
        title: Text(
          "TO DO LIST",
          style: Theme.of(context).textTheme.headline1,
        ),
        centerTitle: true,
        elevation: 3,
        shadowColor: Colors.black,
      ),
      body: ListView.builder(
        itemCount: ToDoList.length,
        itemBuilder: (context, index) {
          return ToDo(
            taskName: ToDoList[index][0],
            taskCompleted: ToDoList[index][1],
            onChanged: (value) => checkBoxChanged(value, index),
            deleteFunction: (context) => deleteTask(index),
          );
        },
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: createNewTask,
        child: Icon(Icons.add),
      ),
    );
  }
}
