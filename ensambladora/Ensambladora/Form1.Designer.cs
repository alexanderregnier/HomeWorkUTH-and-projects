namespace ensambladora
{
    partial class Form1
    {
        /// <summary>
        /// Variable del diseñador necesaria.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Limpiar los recursos que se estén usando.
        /// </summary>
        /// <param name="disposing">true si los recursos administrados se deben desechar; false en caso contrario.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Código generado por el Diseñador de Windows Forms

        /// <summary>
        /// Método necesario para admitir el Diseñador. No se puede modificar
        /// el contenido de este método con el editor de código.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.archivoToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.ventasToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.clientesToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.componentesToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.usuariosToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.salirToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.reportesToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.reporteDeVentasToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.reporteDeUsuariosToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.reporteDeComponentesToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.reporteDeUsuariosToolStripMenuItem1 = new System.Windows.Forms.ToolStripMenuItem();
            this.reporteDeVentasPorClienteToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.reporteDeVentasPorComponentesToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.preferanciasToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.cambiarConstraseñaToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.cambiarIdiomaToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.hacercaDeToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.label1 = new System.Windows.Forms.Label();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.reporteDeVentasPorUsuarioToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.menuStrip1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // menuStrip1
            // 
            this.menuStrip1.ImageScalingSize = new System.Drawing.Size(20, 20);
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.archivoToolStripMenuItem,
            this.reportesToolStripMenuItem,
            this.preferanciasToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Padding = new System.Windows.Forms.Padding(8, 2, 0, 2);
            this.menuStrip1.Size = new System.Drawing.Size(580, 28);
            this.menuStrip1.TabIndex = 0;
            this.menuStrip1.Text = "menuStrip1";
            this.menuStrip1.ItemClicked += new System.Windows.Forms.ToolStripItemClickedEventHandler(this.menuStrip1_ItemClicked);
            // 
            // archivoToolStripMenuItem
            // 
            this.archivoToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.ventasToolStripMenuItem,
            this.clientesToolStripMenuItem,
            this.componentesToolStripMenuItem,
            this.usuariosToolStripMenuItem,
            this.salirToolStripMenuItem});
            this.archivoToolStripMenuItem.Name = "archivoToolStripMenuItem";
            this.archivoToolStripMenuItem.Size = new System.Drawing.Size(71, 24);
            this.archivoToolStripMenuItem.Text = "Archivo";
            // 
            // ventasToolStripMenuItem
            // 
            this.ventasToolStripMenuItem.Name = "ventasToolStripMenuItem";
            this.ventasToolStripMenuItem.Size = new System.Drawing.Size(176, 26);
            this.ventasToolStripMenuItem.Text = "Ventas";
            this.ventasToolStripMenuItem.Click += new System.EventHandler(this.ventasToolStripMenuItem_Click);
            // 
            // clientesToolStripMenuItem
            // 
            this.clientesToolStripMenuItem.Name = "clientesToolStripMenuItem";
            this.clientesToolStripMenuItem.Size = new System.Drawing.Size(176, 26);
            this.clientesToolStripMenuItem.Text = "Clientes";
            this.clientesToolStripMenuItem.Click += new System.EventHandler(this.clientesToolStripMenuItem_Click);
            // 
            // componentesToolStripMenuItem
            // 
            this.componentesToolStripMenuItem.Name = "componentesToolStripMenuItem";
            this.componentesToolStripMenuItem.Size = new System.Drawing.Size(176, 26);
            this.componentesToolStripMenuItem.Text = "Componentes";
            this.componentesToolStripMenuItem.Click += new System.EventHandler(this.componentesToolStripMenuItem_Click);
            // 
            // usuariosToolStripMenuItem
            // 
            this.usuariosToolStripMenuItem.Name = "usuariosToolStripMenuItem";
            this.usuariosToolStripMenuItem.Size = new System.Drawing.Size(176, 26);
            this.usuariosToolStripMenuItem.Text = "Usuarios";
            this.usuariosToolStripMenuItem.Click += new System.EventHandler(this.usuariosToolStripMenuItem_Click);
            // 
            // salirToolStripMenuItem
            // 
            this.salirToolStripMenuItem.Name = "salirToolStripMenuItem";
            this.salirToolStripMenuItem.Size = new System.Drawing.Size(176, 26);
            this.salirToolStripMenuItem.Text = "Salir";
            this.salirToolStripMenuItem.Click += new System.EventHandler(this.salirToolStripMenuItem_Click);
            // 
            // reportesToolStripMenuItem
            // 
            this.reportesToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.reporteDeVentasToolStripMenuItem,
            this.reporteDeUsuariosToolStripMenuItem,
            this.reporteDeComponentesToolStripMenuItem,
            this.reporteDeUsuariosToolStripMenuItem1,
            this.reporteDeVentasPorClienteToolStripMenuItem,
            this.reporteDeVentasPorComponentesToolStripMenuItem,
            this.reporteDeVentasPorUsuarioToolStripMenuItem});
            this.reportesToolStripMenuItem.Name = "reportesToolStripMenuItem";
            this.reportesToolStripMenuItem.Size = new System.Drawing.Size(80, 24);
            this.reportesToolStripMenuItem.Text = "Reportes";
            // 
            // reporteDeVentasToolStripMenuItem
            // 
            this.reporteDeVentasToolStripMenuItem.Name = "reporteDeVentasToolStripMenuItem";
            this.reporteDeVentasToolStripMenuItem.Size = new System.Drawing.Size(322, 26);
            this.reporteDeVentasToolStripMenuItem.Text = "Reporte de Ventas";
            this.reporteDeVentasToolStripMenuItem.Click += new System.EventHandler(this.reporteDeVentasToolStripMenuItem_Click);
            // 
            // reporteDeUsuariosToolStripMenuItem
            // 
            this.reporteDeUsuariosToolStripMenuItem.Name = "reporteDeUsuariosToolStripMenuItem";
            this.reporteDeUsuariosToolStripMenuItem.Size = new System.Drawing.Size(322, 26);
            this.reporteDeUsuariosToolStripMenuItem.Text = "Reporte de Clientes";
            this.reporteDeUsuariosToolStripMenuItem.Click += new System.EventHandler(this.reporteDeUsuariosToolStripMenuItem_Click);
            // 
            // reporteDeComponentesToolStripMenuItem
            // 
            this.reporteDeComponentesToolStripMenuItem.Name = "reporteDeComponentesToolStripMenuItem";
            this.reporteDeComponentesToolStripMenuItem.Size = new System.Drawing.Size(322, 26);
            this.reporteDeComponentesToolStripMenuItem.Text = "Reporte de Componentes";
            this.reporteDeComponentesToolStripMenuItem.Click += new System.EventHandler(this.reporteDeComponentesToolStripMenuItem_Click);
            // 
            // reporteDeUsuariosToolStripMenuItem1
            // 
            this.reporteDeUsuariosToolStripMenuItem1.Name = "reporteDeUsuariosToolStripMenuItem1";
            this.reporteDeUsuariosToolStripMenuItem1.Size = new System.Drawing.Size(322, 26);
            this.reporteDeUsuariosToolStripMenuItem1.Text = "Reporte de Usuarios";
            this.reporteDeUsuariosToolStripMenuItem1.Click += new System.EventHandler(this.reporteDeUsuariosToolStripMenuItem1_Click);
            // 
            // reporteDeVentasPorClienteToolStripMenuItem
            // 
            this.reporteDeVentasPorClienteToolStripMenuItem.Name = "reporteDeVentasPorClienteToolStripMenuItem";
            this.reporteDeVentasPorClienteToolStripMenuItem.Size = new System.Drawing.Size(322, 26);
            this.reporteDeVentasPorClienteToolStripMenuItem.Text = "Reporte de Ventas por Cliente ";
            this.reporteDeVentasPorClienteToolStripMenuItem.Click += new System.EventHandler(this.reporteDeVentasPorClienteToolStripMenuItem_Click);
            // 
            // reporteDeVentasPorComponentesToolStripMenuItem
            // 
            this.reporteDeVentasPorComponentesToolStripMenuItem.Name = "reporteDeVentasPorComponentesToolStripMenuItem";
            this.reporteDeVentasPorComponentesToolStripMenuItem.Size = new System.Drawing.Size(322, 26);
            this.reporteDeVentasPorComponentesToolStripMenuItem.Text = "Reporte de Ventas por Componente";
            this.reporteDeVentasPorComponentesToolStripMenuItem.Click += new System.EventHandler(this.reporteDeVentasPorComponentesToolStripMenuItem_Click);
            // 
            // preferanciasToolStripMenuItem
            // 
            this.preferanciasToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.cambiarConstraseñaToolStripMenuItem,
            this.cambiarIdiomaToolStripMenuItem,
            this.hacercaDeToolStripMenuItem});
            this.preferanciasToolStripMenuItem.Name = "preferanciasToolStripMenuItem";
            this.preferanciasToolStripMenuItem.Size = new System.Drawing.Size(101, 24);
            this.preferanciasToolStripMenuItem.Text = "Preferancias";
            // 
            // cambiarConstraseñaToolStripMenuItem
            // 
            this.cambiarConstraseñaToolStripMenuItem.Name = "cambiarConstraseñaToolStripMenuItem";
            this.cambiarConstraseñaToolStripMenuItem.Size = new System.Drawing.Size(216, 26);
            this.cambiarConstraseñaToolStripMenuItem.Text = "Cambiar contraseña";
            this.cambiarConstraseñaToolStripMenuItem.Click += new System.EventHandler(this.cambiarConstraseñaToolStripMenuItem_Click);
            // 
            // cambiarIdiomaToolStripMenuItem
            // 
            this.cambiarIdiomaToolStripMenuItem.Name = "cambiarIdiomaToolStripMenuItem";
            this.cambiarIdiomaToolStripMenuItem.Size = new System.Drawing.Size(216, 26);
            this.cambiarIdiomaToolStripMenuItem.Text = "Cambiar idioma";
            this.cambiarIdiomaToolStripMenuItem.Click += new System.EventHandler(this.cambiarIdiomaToolStripMenuItem_Click);
            // 
            // hacercaDeToolStripMenuItem
            // 
            this.hacercaDeToolStripMenuItem.Name = "hacercaDeToolStripMenuItem";
            this.hacercaDeToolStripMenuItem.Size = new System.Drawing.Size(216, 26);
            this.hacercaDeToolStripMenuItem.Text = "Hacerca de...";
            this.hacercaDeToolStripMenuItem.Click += new System.EventHandler(this.hacercaDeToolStripMenuItem_Click);
            // 
            // label1
            // 
            this.label1.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 350);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(65, 17);
            this.label1.TabIndex = 1;
            this.label1.Text = "Usuario: ";
            this.label1.Click += new System.EventHandler(this.label1_Click);
            // 
            // pictureBox1
            // 
            this.pictureBox1.Image = ((System.Drawing.Image)(resources.GetObject("pictureBox1.Image")));
            this.pictureBox1.Location = new System.Drawing.Point(199, 31);
            this.pictureBox1.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(285, 290);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.pictureBox1.TabIndex = 2;
            this.pictureBox1.TabStop = false;
            // 
            // reporteDeVentasPorUsuarioToolStripMenuItem
            // 
            this.reporteDeVentasPorUsuarioToolStripMenuItem.Name = "reporteDeVentasPorUsuarioToolStripMenuItem";
            this.reporteDeVentasPorUsuarioToolStripMenuItem.Size = new System.Drawing.Size(322, 26);
            this.reporteDeVentasPorUsuarioToolStripMenuItem.Text = "Reporte de ventas por Usuario";
            this.reporteDeVentasPorUsuarioToolStripMenuItem.Click += new System.EventHandler(this.reporteDeVentasPorUsuarioToolStripMenuItem_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.White;
            this.ClientSize = new System.Drawing.Size(580, 375);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.menuStrip1);
            this.MainMenuStrip = this.menuStrip1;
            this.Margin = new System.Windows.Forms.Padding(4);
            this.Name = "Form1";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Sistema Ensambladora";
            this.WindowState = System.Windows.Forms.FormWindowState.Maximized;
            this.Load += new System.EventHandler(this.Form1_Load);
            this.Resize += new System.EventHandler(this.Form1_Resize);
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem archivoToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem ventasToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem clientesToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem componentesToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem salirToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem reportesToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem reporteDeVentasToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem reporteDeUsuariosToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem reporteDeComponentesToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem reporteDeVentasPorClienteToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem reporteDeVentasPorComponentesToolStripMenuItem;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.ToolStripMenuItem usuariosToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem reporteDeUsuariosToolStripMenuItem1;
        private System.Windows.Forms.ToolStripMenuItem preferanciasToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem cambiarConstraseñaToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem cambiarIdiomaToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem hacercaDeToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem reporteDeVentasPorUsuarioToolStripMenuItem;
    }
}

