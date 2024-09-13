using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ensambladora
{
    public partial class Form1 : Form
    {
        public static string cuenta = "", nivel = "0", idioma = "0";
        public Form1()
        {
            InitializeComponent();
        }

        private void salirToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void ventasToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Form3 f3 = new Form3();
            f3.Show();
        }

        private void clientesToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Form4 f4 = new Form4();
            f4.Show();
        }

        private void componentesToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Form5 f5 = new Form5();
            f5.Show();
        }

        private void reporteDeVentasToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Form6 f6 = new Form6();
            f6.Show();
        }
        private void reporteDeUsuariosToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Form7 f7 = new Form7();
            f7.Show();
        }

        private void reporteDeComponentesToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Form8 f8 = new Form8();
            f8.Show();
        }

        private void reporteDeVentasPorClienteToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Form9 f9 = new Form9();
            f9.Show();
        }

        private void reporteDeVentasPorComponentesToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Form10 f10 = new Form10();
            f10.Show();
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            pictureBox1.Left = (this.Width / 2) - (pictureBox1.Width / 2);
            pictureBox1.Top = (this.Height / 2) - (pictureBox1.Height / 2);
        }

        private void menuStrip1_ItemClicked(object sender, ToolStripItemClickedEventArgs e)
        {

        }

        private void usuariosToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Form11 f11 = new Form11();
            f11.Show();
        }

        private void reporteDeUsuariosToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            Form12 f12 = new Form12();
            f12.Show();
        }

        private void cambiarConstraseñaToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Form13 f13 = new Form13();
            f13.Show();
        }

        private void cambiarIdiomaToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Form14 f14 = new Form14();
            f14.Show();
        }

        private void hacercaDeToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Form15 f15 = new Form15();
            f15.Show();
        }

        private void reporteDeVentasPorUsuarioToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Form16 f16 = new Form16();
            f16.Show();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Form2 f2 = new Form2();
            f2.ShowDialog();
            if (nivel == "1")
            {
                label1.Text = "Usuario: " + cuenta + " (administrador)";
            }else
            {
                label1.Text = "Usuario: " + cuenta + " (operador)";
            }

            if (idioma=="2")
            {
                this.archivoToolStripMenuItem.Text = "File";
                this.ventasToolStripMenuItem.Text = "Sales";
                this.clientesToolStripMenuItem.Text = "Customers";
                this.componentesToolStripMenuItem.Text = "Components";
                this.usuariosToolStripMenuItem.Text = "Users";
                this.salirToolStripMenuItem.Text = "Exit";

                this.reportesToolStripMenuItem.Text = "Reports";
                this.reporteDeVentasToolStripMenuItem.Text = "Sales reports";
                this.reporteDeUsuariosToolStripMenuItem.Text = "Customer reports";
                this.reporteDeComponentesToolStripMenuItem.Text = "Component Reports";
                this.reporteDeUsuariosToolStripMenuItem1.Text = "Users Reports";
                this.reporteDeVentasPorClienteToolStripMenuItem.Text = "Sales Report by Customer";
                this.reporteDeVentasPorComponentesToolStripMenuItem.Text = "Sales Report by Component";

                this.preferanciasToolStripMenuItem.Text = "Preferences";
                this.cambiarConstraseñaToolStripMenuItem.Text = "Change password";
                this.cambiarIdiomaToolStripMenuItem.Text = "Change language";
                this.hacercaDeToolStripMenuItem.Text = "About...";


                this.label1.Text = "User: ";
                this.Text = "System Assembler";
            }

        }
    }
}
