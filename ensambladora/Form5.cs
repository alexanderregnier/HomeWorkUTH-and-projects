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
    public partial class Form5 : Form
    {
        public Form5()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string connectionString = "datasource=localhost;port=3307;username=root;password=1234;database=ensambladora;";
            string query = "Select * from componentes";
            MySqlConnection databaseConnection = new MySqlConnection(connectionString);
            MySqlCommand commandDatabase = new MySqlCommand(query, databaseConnection);
            MySqlDataReader reader;
            dataGridView1.Rows.Clear();
            try
            {
                databaseConnection.Open();
                reader = commandDatabase.ExecuteReader();
                if (reader.HasRows)
                {
                    while (reader.Read())
                    {
                        dataGridView1.Rows.Add(reader.GetString(0), reader.GetString(1), reader.GetString(2),
                        reader.GetString(3));
                    }
                }
                else
                {
                    MessageBox.Show("No se encontraron datos.");
                }
                databaseConnection.Close();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string connectionString = "datasource=localhost;port=3307;username=root;password=1234;database=ensambladora;";
            string query = "insert into componentes values(null,'" + textBox3.Text + "','" + textBox4.Text + "','"
            + textBox5.Text + "')";
            MySqlConnection databaseConnection = new MySqlConnection(connectionString);
            MySqlCommand commandDatabase = new MySqlCommand(query, databaseConnection);
            MySqlDataReader reader;
            databaseConnection.Open();
            reader = commandDatabase.ExecuteReader();
            databaseConnection.Close();
            button1_Click(sender, e); //Buscar
        }

        private void button3_Click(object sender, EventArgs e)
        {
            string connectionString = "datasource=localhost;port=3307;username=root;password=1234;database=ensambladora;";
            string query = "delete from componentes where id_componen=" + textBox2.Text;
            MySqlConnection databaseConnection = new MySqlConnection(connectionString);
            MySqlCommand commandDatabase = new MySqlCommand(query, databaseConnection);
            MySqlDataReader reader;
            databaseConnection.Open();
            reader = commandDatabase.ExecuteReader();
            databaseConnection.Close();
            button1_Click(sender, e); //Buscar
        }

        private void button4_Click(object sender, EventArgs e)
        {
            string connectionString = "datasource=localhost;port=3307;username=root;password=1234;database=ensambladora;";
            string query = "update componentes set componente='"
            + textBox3.Text.Trim() + "', precio='"
            + textBox4.Text.Trim() + "', Disponible='"
            + textBox5.Text.Trim() + "' where id_componen=" + textBox2.Text;
            MySqlConnection databaseConnection = new MySqlConnection(connectionString);
            MySqlCommand commandDatabase = new MySqlCommand(query, databaseConnection);
            MySqlDataReader reader;
            try
            {
                databaseConnection.Open();
                reader = commandDatabase.ExecuteReader();
                databaseConnection.Close();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
            button1_Click(sender, e); //Buscar
        }

        private void button5_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {
            
        }

        private void dataGridView1_CellClick(object sender, DataGridViewCellEventArgs e)
        {
            if (e.RowIndex != -1)
            {
                textBox2.Text = dataGridView1.Rows[e.RowIndex].Cells[0].Value.ToString();
                textBox3.Text = dataGridView1.Rows[e.RowIndex].Cells[1].Value.ToString();
                textBox4.Text = dataGridView1.Rows[e.RowIndex].Cells[2].Value.ToString();
                textBox5.Text = dataGridView1.Rows[e.RowIndex].Cells[3].Value.ToString();
            }
        }

        private void Form5_Load(object sender, EventArgs e)
        {
            if (Form1.idioma == "2")
            {
                this.button5.Text = "Exit"; 
                this.button4.Text = "modify";
                this.button3.Text = "Delete";
                this.button2.Text = "Add";
                this.button1.Text = "search";
            }
        }

        private void textBox2_Leave(object sender, EventArgs e)
        {
            Int64 n;
            if (textBox2.Text != "")
            {
                try
                {
                    n = Convert.ToInt64(textBox2.Text);
                }
                catch (Exception xx)
                {
                    MessageBox.Show("El formato no es correcto.\nAcepta solo digitos\n" + xx.Message);
                    textBox2.Focus();
                }
            }
        }

        private void textBox3_Leave(object sender, EventArgs e)
        {
            String n;
            if (textBox3.Text != "")
            {
                try
                {
                    n = Convert.ToString(textBox3.Text);
                }
                catch (Exception xx)
                {
                    MessageBox.Show("El formato no es correcto.\nAcepta solo digitos\n" + xx.Message);
                    textBox3.Focus();
                }
            }
        }

        private void textBox4_Leave(object sender, EventArgs e)
        {
            double n;
            if (textBox4.Text != "")
            {
                try
                {
                    n = Convert.ToDouble(textBox4.Text);
                }
                catch (Exception xx)
                {
                    MessageBox.Show("El formato no es correcto.\nAcepta solo digitos\n" + xx.Message);
                    textBox4.Focus();
                }
            }
        }

        private void textBox5_Leave(object sender, EventArgs e)
        {
            Int64 n;
            if (textBox5.Text != "")
            {
                try
                {
                    n = Convert.ToInt64(textBox5.Text);
                }
                catch (Exception xx)
                {
                    MessageBox.Show("El formato no es correcto.\nAcepta solo digitos\n" + xx.Message);
                    textBox5.Focus();
                }
            }
        }
    }
}
