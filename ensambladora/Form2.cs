using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using MySql.Data.MySqlClient;

namespace ensambladora
{
    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
        }
        int intentos = 0;
        private void button1_Click(object sender, EventArgs e)
        {
            string connectionString = "datasource=localhost;port=3307;username=root;password=1234;database=ensambladora;";
            string query = "Select nivel, idioma from usuarios where cuenta='" + textBox1.Text
                + "'and clave=md5('" + textBox2.Text + "')";
            MySqlConnection databaseConnection = new MySqlConnection(connectionString);
            MySqlCommand commandDatabase = new MySqlCommand(query, databaseConnection);
            MySqlDataReader reader;
            try
            {
                databaseConnection.Open();
                reader = commandDatabase.ExecuteReader();
                if (reader.HasRows)
                {
                    reader.Read();
                    Form1.cuenta = textBox1.Text;
                    Form1.nivel = reader.GetString(0);
                    Form1.idioma = reader.GetString(1);
                    Close();
                }
                else
                {
                    MessageBox.Show("cuenta o clave no es correcta");
                    intentos++;
                    if (intentos >= 3) Application.Exit();
                }
            }
            catch (Exception)
            {
                MessageBox.Show("Error al autenticar usuario.");
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void Form2_FormClosed(object sender, FormClosedEventArgs e)
        {
              if (Form1.cuenta == "") Application.Exit();
        }

        private void Form2_Load(object sender, EventArgs e)
        {
            this.Text = "Sales";
            button1.Text = "Accept";
            button2.Text = "Cancel";

            this.label1.Text = "User";
            this.label2.Text = "Password";
            this.button1.Text = "Accept";
            this.button2.Text = "Cancel";
        }
    }
}