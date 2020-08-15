#! /usr/bin/env python
class CNN_Model(nn.Module):
    def __init__(self):
        super(CNN_Model, self).__init__()
        self.conv1 = nn.Sequential(         
            nn.Conv2d(
                in_channels=3,              
                out_channels=32,            
                kernel_size=4,              
                stride=1,                   
                padding=0,                  
            ),                                                 
            nn.MaxPool2d(kernel_size=2, stride=2),    
        )
        self.conv2 = nn.Sequential(         
            nn.Conv2d(
                in_channels=32,
                out_channels=32,
                kernel_size=4,
                stride=1,
                padding=0,
            ),                           
            nn.MaxPool2d(kernel_size=2, stride=2),                
        )
        self.conv3 = nn.Sequential(         
            nn.Conv2d(
                in_channels=32,
                out_channels=32,
                kernel_size=4,
                stride=1,
                padding=0,
            ),                           
            nn.MaxPool2d(kernel_size=2, stride=2),                
        )
        self.conv4 = nn.Sequential(         
            nn.Conv2d(
                in_channels=32,
                out_channels=32,
                kernel_size=4,
                stride=1,
                padding=1,
            ),                           
            nn.MaxPool2d(kernel_size=2, stride=2),                
        )
        self.fc1 = nn.Linear(800, 200)
        self.fc2 = nn.Linear(200, 3)

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = self.conv3(x)
        x = self.conv4(x)
        x = x.view(x.size(0), -1)
        x = self.fc1(x)
        x = self.fc2(x)
        return x