class UploadScreen extends StatefulWidget {
  @override
  _UploadScreenState createState() => _UploadScreenState();
}

class _UploadScreenState extends State<UploadScreen> {
  File? logFile, videoFile;

  Future<void> upload() async {
    final response = await http.post(
      Uri.parse('http://api.fpvanalyzer.dev/api/upload'),
      files: [
        http.MultipartFile('log_file', logFile!.readAsBytes().asStream(), logFile!.lengthSync(), filename: logFile!.path.split('/').last),
      ],
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Upload Flight')),
      body: Center(child: ElevatedButton(onPressed: upload, child: Text('Upload'))),
    );
  }
}