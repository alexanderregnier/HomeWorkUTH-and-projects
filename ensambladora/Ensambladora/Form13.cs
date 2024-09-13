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
    public partial class Form13 : Form
    {
        public Form13()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void button1_Click(object sender, EventArgs e)
        {//Boton aceptar de cambiar contraseña
            if (textBox1.Text == "" || textBox2.Text == "" || textBox3.Text == "")
            {
                MessageBox.Show("Los datos requeridos no estan completos.");
            }
            else
            {
                if (textBox2.Text == textBox3.Text)
                {
                    string connectionString = "datasource=localhost;port=3307;username=root;password=1234;database=ensambladora;";
                    string query = "update Usuarios set clave=md5('" + textBox2.Text + "') where cuenta='" + Form1.cuenta
                        + "' and clave=md5('" + textBox1.Text + "')";
                    MySqlConnection databaseConnection = new MySqlConnection(connectionString);
                    MySqlCommand commandDatabase = new MySqlCommand(query, databaseConnection);
                    int reader;
                    try
                    {
                        databaseConnection.Open();
                        reader = commandDatabase.ExecuteNonQuery();
                        if (reader != 0)
                        {
                            MessageBox.Show("Se modifico la clave Exitosamente.");
                            Close();
                        }
                        else
                        {
                            MessageBox.Show("La contraseña no es correcta.");
                        }
                        
                    }
                    catch (Exception) { }
                }
                else
                {
                    MessageBox.Show("La nueva clave y su repeticion no son iguales.");
                }
            }
        }

        private void Form13_Load(object sender, EventArgs e)
        {

        }
    }
}
