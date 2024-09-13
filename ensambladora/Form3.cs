using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using MySql.Data.MySqlClient;
using System.Windows.Forms;

namespace ensambladora
{
    public partial class Form3 : Form
    {
        public Form3()
        {
            InitializeComponent();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string connectionString = "datasource=localhost;port=3307;username=root;password=1234;database=ensambladora;";
            string query = "insert into ventas values(null,'" + textBox3.Text + "','" + textBox4.Text + "','"
            + textBox5.Text + "','" + textBox6.Text.Substring(6, 4) + textBox6.Text.Substring(3, 2) + textBox6.Text.Substring(0, 2) + "')";
            MySqlConnection databaseConnection = new MySqlConnection(connectionString);
            MySqlCommand commandDatabase = new MySqlCommand(query, databaseConnection);
            MySqlDataReader reader;
            databaseConnection.Open();
            reader = commandDatabase.ExecuteReader();
            databaseConnection.Close();
            button1_Click(sender, e); //Buscar

        }

        private void Form3_Load(object sender, EventArgs e)
        {
            if (Form1.idioma == "2")
            {
                this.Text = "Sales";
                button1.Text = "Search";
                button2.Text = "Add";
                button3.Text = "Delete";
                button4.Text = "Update";
                button5.Text = "Exit";

                this.button1.Text = "Search";
                this.button2.Text = "Add";
                this.button3.Text = "Delete";
                this.button4.Text = "Modify";
                this.button5.Text = "Exit";
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string connectionString = "datasource=localhost;port=3307;username=root;password=1234;database=ensambladora;";
            string query = "Select * from ventas";
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
                        reader.GetString(3), reader.GetString(4));
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

        private void button3_Click(object sender, EventArgs e)
        {
            string connectionString = "datasource=localhost;port=3307;username=root;password=1234;database=ensambladora;";
            string query = "delete from ventas where id_ventas=" + textBox2.Text;
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
            string query = "update ventas set id_cliente='"
            + textBox3.Text + "', id_componen='"
            + textBox4.Text + "', Monto='"
            + textBox5.Text + "', FechaHora='"
            + textBox6.Text.Substring(6, 4) + textBox6.Text.Substring(3, 2) + textBox6.Text.Substring(0, 2) + "' where id_ventas=" + textBox2.Text;
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
                textBox6.Text = dataGridView1.Rows[e.RowIndex].Cells[4].Value.ToString();
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
            Int64 n;
            if (textBox3.Text != "")
            {
                try
                {
                    n = Convert.ToInt64(textBox3.Text);
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
            Int64 n;
            if (textBox4.Text != "")
            {
                try
                {
                    n = Convert.ToInt64(textBox4.Text);
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
            double n;
            if (textBox5.Text != "")
            {
                try
                {
                    n = Convert.ToDouble(textBox5.Text);
                }
                catch (Exception xx)
                {
                    MessageBox.Show("El formato no es correcto.\nAcepta solo Decimales\n" + xx.Message);
                    textBox5.Focus();
                }
            }
        }

        private void textBox6_Leave(object sender, EventArgs e)
        {
            DateTime n;
            if (textBox6.Text != "")
            {
                try
                {
                    n = Convert.ToDateTime(textBox6.Text);
                }
                catch (Exception xx)
                {
                    MessageBox.Show("El formato no es correcto.\nAcepta solo Fechas dd/mm/aaaa\n" + xx.Message);
                    textBox6.Focus();
                }
            }
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }
    }
}
