# Facial Attendance Machine

A face recognition-based attendance monitoring system designed to enhance and upgrade traditional attendance systems in educational institutions and workplaces.

## 🔗 Repository
[https://github.com/aeiou-sudo/Facial-Attendance-Machine.git](https://github.com/aeiou-sudo/Facial-Attendance-Machine.git)

## 📋 Overview

The Facial Attendance Machine is an automated attendance system that uses face recognition technology to track employee/student attendance. The system eliminates the need for manual attendance marking, reduces fraud possibilities, and provides real-time attendance monitoring with mood analysis as an additional feature.

## ✨ Features

- **Face Recognition**: Automated face detection and recognition using VGGFace with ResNet50 model
- **Real-time Processing**: Live video feed processing with MTCNN face detection
- **Attendance Tracking**: Automatic marking of entry and exit times
- **Mood Analysis**: Facial expression analysis to determine individual mood (additional feature)
- **Admin Portal**: Administrative interface for managing face database and attendance records
- **User Portal**: Portal for users to track their attendance progress
- **CSV Reports**: Daily attendance reports generated in CSV format
- **Duplicate Prevention**: Prevents proxy attendance through accurate face matching

## 🛠️ Technology Stack

### Platform & IDE
- **Platform**: Anaconda
- **IDE**: Jupyter Notebook
- **Programming Language**: Python

### Libraries & Frameworks
- **Face Detection**: MTCNN (Multi-task Convolutional Neural Networks)
- **Face Recognition**: Keras VGGFace with ResNet50
- **Computer Vision**: OpenCV (cv2)
- **Image Processing**: PIL (Python Imaging Library)
- **Numerical Computing**: NumPy
- **Data Visualization**: Matplotlib
- **Distance Calculation**: SciPy

## 📁 Project Structure

```
Facial-Attendance-Machine/
├── images/                     # Training face images
├── Encodings/                  # Stored face encodings
├── Face_Registration.py        # Face registration module
├── Face_Encoding.py           # Face encoding generation
├── Facial_Attendance.py       # Main attendance system
├── [date].csv                 # Daily attendance reports
└── README.md
```

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/aeiou-sudo/Facial-Attendance-Machine.git
   cd Facial-Attendance-Machine
   ```

2. **Install required dependencies**
   ```bash
   pip install opencv-python
   pip install mtcnn
   pip install keras-vggface
   pip install tensorflow
   pip install pillow
   pip install numpy
   pip install matplotlib
   pip install scipy
   ```

3. **Create required directories**
   ```bash
   mkdir images
   mkdir Encodings
   ```

## 📖 Usage

### 1. Face Registration
Run the face registration script to add new users to the system:
```bash
python Face_Registration.py
```
- Position yourself in front of the camera
- Press `Space` to capture your face
- Enter your name when prompted
- The system will automatically generate and store face encodings

### 2. Generate Face Encodings
Process all registered faces to create encodings:
```bash
python Face_Encoding.py
```

### 3. Start Attendance System
Launch the main attendance monitoring system:
```bash
python Facial_Attendance.py
```
- The system will start the camera feed
- Face detection and recognition will happen in real-time
- Attendance will be automatically marked when faces are recognized
- Press `q` to quit the system

## 📊 Attendance Reports

The system generates daily CSV reports with the following information:
- **Name**: Employee/Student name
- **Time In**: Entry time
- **Time Out**: Exit time
- **Presence Status**: FULL/HALF/NA based on duration
- **Hours**: Total hours present

## ⚙️ System Requirements

- **Operating System**: Windows, Linux, or macOS
- **Python**: 3.6 or higher
- **Camera**: Webcam or external camera
- **Memory**: Minimum 4GB RAM recommended
- **Storage**: Sufficient space for face images and encodings

## 🔧 Configuration

### Threshold Settings
- **Recognition Threshold**: 0.3 (cosine distance)
- **Minimum Time Difference**: 1 minute for exit detection
- **Full Day**: 3+ minutes (configurable in code)
- **Half Day**: 2+ minutes (configurable in code)

### Customization
You can modify the following parameters in the code:
- Recognition threshold for face matching
- Time thresholds for attendance classification
- Image resolution and quality settings
- Database storage locations

## 🎯 Key Algorithms

1. **MTCNN**: Multi-task Convolutional Neural Networks for face detection
2. **VGGFace ResNet50**: Deep learning model for face feature extraction
3. **Cosine Distance**: Similarity measurement for face matching
4. **Real-time Processing**: Frame-by-frame video analysis

## 👥 Team

This project was developed by students from Mar Baselios Institute of Technology and Science (MBITS):

- **Paul Jose** (MBI18CS040)
- **Joju Sunny** (MBI18CS031) 
- **Muhammed Safil P H** (MBI18CS037)

**Project Guide**: Asst. Prof. Mahesh K M  
**Project Coordinator**: Asst. Prof. Mintu Thomas  
**HOD**: Midhun Mathew

## 📝 License

This project is part of an academic submission to APJ Abdul Kalam Technological University for the Bachelor of Technology degree in Computer Science and Engineering.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/aeiou-sudo/Facial-Attendance-Machine/issues).

## 📞 Support

For support or questions about this project, please create an issue in the GitHub repository.

## 🔮 Future Enhancements

- Integration with mobile applications
- Cloud-based storage and processing
- Multi-camera support
- Enhanced mood analysis features
- Integration with existing HR/Student management systems
- Web-based dashboard for better visualization

---

**Note**: This system is designed for educational and institutional use. Ensure proper privacy considerations and user consent before deployment in production environments.
