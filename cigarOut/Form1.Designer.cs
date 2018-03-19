namespace cigarOut
{
    partial class cigarOut
    {
        /// <summary>
        /// 必需的设计器变量。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清理所有正在使用的资源。
        /// </summary>
        /// <param name="disposing">如果应释放托管资源，为 true；否则为 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows 窗体设计器生成的代码

        /// <summary>
        /// 设计器支持所需的方法 - 不要
        /// 使用代码编辑器修改此方法的内容。
        /// </summary>
        private void InitializeComponent()
        {
            this.header = new System.Windows.Forms.Label();
            this.telegraphNumber = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.telegraphContent = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.telegraphSize = new System.Windows.Forms.Label();
            this.sendStrings = new System.Windows.Forms.TextBox();
            this.send = new System.Windows.Forms.Button();
            this.lab = new System.Windows.Forms.Label();
            this.ip = new System.Windows.Forms.TextBox();
            this.connect = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // header
            // 
            this.header.AutoSize = true;
            this.header.Location = new System.Drawing.Point(12, 61);
            this.header.Name = "header";
            this.header.Size = new System.Drawing.Size(65, 12);
            this.header.TabIndex = 0;
            this.header.Text = "电文编号：";
            // 
            // telegraphNumber
            // 
            this.telegraphNumber.Location = new System.Drawing.Point(71, 58);
            this.telegraphNumber.Name = "telegraphNumber";
            this.telegraphNumber.Size = new System.Drawing.Size(117, 21);
            this.telegraphNumber.TabIndex = 1;
            this.telegraphNumber.Text = "C1T101";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 93);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(65, 12);
            this.label2.TabIndex = 0;
            this.label2.Text = "数据内容：";
            // 
            // telegraphContent
            // 
            this.telegraphContent.Location = new System.Drawing.Point(71, 90);
            this.telegraphContent.Name = "telegraphContent";
            this.telegraphContent.Size = new System.Drawing.Size(353, 21);
            this.telegraphContent.TabIndex = 1;
            this.telegraphContent.Text = "RUN04530820151202121130";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 123);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(65, 12);
            this.label1.TabIndex = 0;
            this.label1.Text = "电文长度：";
            // 
            // telegraphSize
            // 
            this.telegraphSize.AutoSize = true;
            this.telegraphSize.Location = new System.Drawing.Point(83, 123);
            this.telegraphSize.Name = "telegraphSize";
            this.telegraphSize.Size = new System.Drawing.Size(11, 12);
            this.telegraphSize.TabIndex = 2;
            this.telegraphSize.Text = "0";
            // 
            // sendStrings
            // 
            this.sendStrings.Location = new System.Drawing.Point(14, 153);
            this.sendStrings.Multiline = true;
            this.sendStrings.Name = "sendStrings";
            this.sendStrings.ScrollBars = System.Windows.Forms.ScrollBars.Both;
            this.sendStrings.Size = new System.Drawing.Size(410, 155);
            this.sendStrings.TabIndex = 3;
            // 
            // send
            // 
            this.send.Location = new System.Drawing.Point(349, 29);
            this.send.Name = "send";
            this.send.Size = new System.Drawing.Size(75, 43);
            this.send.TabIndex = 4;
            this.send.Text = "Send";
            this.send.UseVisualStyleBackColor = true;
            this.send.Click += new System.EventHandler(this.send_Click);
            // 
            // lab
            // 
            this.lab.AutoSize = true;
            this.lab.Location = new System.Drawing.Point(12, 30);
            this.lab.Name = "lab";
            this.lab.Size = new System.Drawing.Size(29, 12);
            this.lab.TabIndex = 0;
            this.lab.Text = "IP：";
            this.lab.TextAlign = System.Drawing.ContentAlignment.TopRight;
            // 
            // ip
            // 
            this.ip.Location = new System.Drawing.Point(71, 27);
            this.ip.Name = "ip";
            this.ip.Size = new System.Drawing.Size(117, 21);
            this.ip.TabIndex = 1;
            this.ip.Text = "10.130.161.59";
            // 
            // connect
            // 
            this.connect.Location = new System.Drawing.Point(227, 27);
            this.connect.Name = "connect";
            this.connect.Size = new System.Drawing.Size(75, 46);
            this.connect.TabIndex = 4;
            this.connect.Text = "Connect";
            this.connect.UseVisualStyleBackColor = true;
            this.connect.Click += new System.EventHandler(this.connect_Click);
            // 
            // cigarOut
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(438, 320);
            this.Controls.Add(this.connect);
            this.Controls.Add(this.send);
            this.Controls.Add(this.sendStrings);
            this.Controls.Add(this.telegraphSize);
            this.Controls.Add(this.telegraphContent);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.ip);
            this.Controls.Add(this.telegraphNumber);
            this.Controls.Add(this.lab);
            this.Controls.Add(this.header);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedToolWindow;
            this.Name = "cigarOut";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "CigarOut";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label header;
        private System.Windows.Forms.TextBox telegraphNumber;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox telegraphContent;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label telegraphSize;
        private System.Windows.Forms.TextBox sendStrings;
        private System.Windows.Forms.Button send;
        private System.Windows.Forms.Label lab;
        private System.Windows.Forms.TextBox ip;
        private System.Windows.Forms.Button connect;
    }
}

