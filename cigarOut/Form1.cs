using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Net.Sockets;
using System.Net;
using System.Threading;

namespace cigarOut
{
    public partial class cigarOut : Form
    {
        Socket clientSocket = null;

        /**
         * 0 : don't connect
         * 1 : conect 
         * 2 : send except
         * 3 : receive except
         */
        int conectStatus = 0;

        public cigarOut()
        {
            InitializeComponent();
        }

        private void connect_Click(object sender, EventArgs e)
        {
            if (connect.Text.Equals("Connect"))
            {

                IPAddress ipaddr = IPAddress.Parse(ip.Text);
                clientSocket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
                try
                {
                    clientSocket.Connect(new IPEndPoint(ipaddr, 8088)); //配置服务器IP与端口  
                    this.conectStatus = 1;
                    Console.WriteLine("连接服务器成功");
                }
                catch
                {
                    Console.WriteLine("连接服务器失败，请按回车键退出！");
                    return;
                }

                Thread receiveThread = new Thread(ReceiveMessage);
                receiveThread.Start(clientSocket);

                Thread sendThread = new Thread(SendMessage);
                sendThread.Start(clientSocket);

                connect.Text = "Close";
            }
            else
            {
                if (clientSocket != null)
                {
                    clientSocket.Close();
                    clientSocket = null;
                }

                connect.Text = "Connect";
            }
        }
        /// <summary>  
        /// 接收消息  
        /// </summary>  
        /// <param name="clientSocket"></param>  
        private void ReceiveMessage(object clientSocket)
        {
            Socket myClientSocket = (Socket)clientSocket;
            byte[] result = new byte[1024];
            // 设置20s未接收到心跳包超时，会引发异常
            myClientSocket.ReceiveTimeout = 20000;

            while (true)
            {
                try
                {
                    //通过clientSocket接收数据  
                    int receiveNumber = myClientSocket.Receive(result);
                    if (receiveNumber != 0)
                    {
                        Action<String> AsyncUIDelegate1 = delegate(string n) { sendStrings.AppendText(n); };
                        telegraphContent.Invoke(AsyncUIDelegate1, "Receive " + receiveNumber + " bytes: " + Encoding.ASCII.GetString(result, 0, receiveNumber));
                    }
                    else
                    {
                        this.conectStatus = 3;
                        connect.Text = "Connect";
                        clientSocket = null;
                        break;
                    }
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex.Message);
                    Console.WriteLine("connect receive data except.");

                    switch (this.conectStatus)
                    {
                        case 1:
                            this.conectStatus = 3;
                            Action<String> AsyncUIDelegate1 = delegate(string n) { connect.Enabled = false;};
                            telegraphContent.Invoke(AsyncUIDelegate1, "");
                            break;
                        case 2:
                            Action<String> AsyncUIDelegate2 = delegate(string n) { connect.Text = "Connect"; connect.Refresh(); connect.Enabled = true;};
                            telegraphContent.Invoke(AsyncUIDelegate2, "");
                            clientSocket = null;
                            break;
                        default:
                            break;
                    }

                    break;
                }
            }
        }

        /// <summary>  
        /// 接收消息  
        /// </summary>  
        /// <param name="clientSocket"></param>  
        private void SendMessage(object clientSocket)
        {
            Socket myClientSocket = (Socket)clientSocket;
            byte[] result = new byte[1024];
            // 设置20s未接收到心跳包超时，会引发异常
            myClientSocket.ReceiveTimeout = 20000;

            while (true)
            {
                try
                {
                    string sendString = "C1T1990002\r\n";
                    myClientSocket.Send(System.Text.Encoding.Default.GetBytes(sendString));

                    Action<String> AsyncUIDelegate1 = delegate(string n) { sendStrings.AppendText(n); };
                    telegraphContent.Invoke(AsyncUIDelegate1, "Send " + sendString.Length + " bytes: " + sendString);

                    Thread.Sleep(10000);
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex.Message);
                    Console.WriteLine("connect send heatbeat data except.");

                    switch (this.conectStatus)
                    {
                        case 1:
                            this.conectStatus = 2;
                            Action<String> AsyncUIDelegate1 = delegate(string n) { connect.Enabled = false;};
                            telegraphContent.Invoke(AsyncUIDelegate1, "");
                            break;
                        case 3:
                            Action<String> AsyncUIDelegate2 = delegate(string n) { connect.Text = "Connect"; connect.Refresh(); connect.Enabled = true;};
                            telegraphContent.Invoke(AsyncUIDelegate2, "");
                            clientSocket = null;
                            break;
                        default:
                            break;
                    }

                    break;
                }
            }
        }

        private void send_Click(object sender, EventArgs e)
        {
            if (clientSocket == null)
                return;

            try
            {
                StringBuilder sendString = new StringBuilder();

                int count = 0;
                String content = "";
                String header = "";
                Action<String> AsyncUIDelegate = delegate(string n) { 
                    header = telegraphNumber.Text; 
                    count = telegraphContent.TextLength + 2;  // 2 just for end of a line "\r\n："
                    content = telegraphContent.Text;
                    telegraphSize.Text = count.ToString();
                };
                telegraphContent.Invoke(AsyncUIDelegate, "");

                sendString.Append(header);
                sendString.Append(String.Format("{0:0000}", count));
                sendString.Append(content);
                sendString.Append("\r\n");

                // Console.WriteLine(sendString);

                //通过clientSocket接收数据  
                
                // int receiveNumber = myClientSocket.Send(result);
                // Console.WriteLine("接收客户端{0}消息{1}", myClientSocket.RemoteEndPoint.ToString(), Encoding.ASCII.GetString(result, 0, receiveNumber));

                clientSocket.Send(System.Text.Encoding.Default.GetBytes(sendString.ToString()));

                Action<String> AsyncUIDelegate1 = delegate(string n) { sendStrings.AppendText(n); };
                telegraphContent.Invoke(AsyncUIDelegate1, "Send " + sendString.Length + " bytes: " + sendString);

                Console.WriteLine("zengjf");

            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }

        }
    }
}
