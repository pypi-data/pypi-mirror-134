#include "config.h"

#define LIBSSH_STATIC

#include "torture.h"
#include "dh-gex.c"

static const char moduli_content[] =
    "# Time Type Tests Tries Size Generator Modulus\n"
    "20120821044040 2 6 100 1023 5 D9277DAA27DB131C03B108D41A76B4DA8ACEECCCAE73"
    "D2E48CEDAAA70B09EF9F04FB020DCF36C51B8E485B26FABE0337E24232BE4F4E6935483102"
    "44937433FB1A5758195DC73B84ADEF8237472C46747D79DC0A2CF8A57CE8DBD8F466A20F85"
    "51E7B1B824B2E4987A8816D9BC0741C2798F3EBAD3ADEBCC78FCE6A770E2EC9F\n"
    "20120821044502 2 6 100 1535 5 D1391174233D315398FE2830AC6B2B66BCCD01B0A634"
    "899F339B7879F1DB85712E9DC4E4B1C6C8355570C1D2DCB53493DF18175A9C53D1128B592B"
    "4C72D97136F5542FEB981CBFE8012FDD30361F288A42BD5EBB08BAB0A5640E1AC48763B2AB"
    "D1945FEE36B2D55E1D50A1C86CED9DD141C4E7BE2D32D9B562A0F8E2E927020E91F58B57EB"
    "9ACDDA106A59302D7E92AD5F6E851A45FA1CFE86029A0F727F65A8F475F33572E2FDAB6073"
    "F0C21B8B54C3823DB2EF068927E5D747498F96361507\n"
    "20120821050636 2 6 100 2047 2 DD2047CBDBB6F8E919BC63DE885B34D0FD6E3DB2887D"
    "8B46FE249886ACED6B46DFCD5553168185FD376122171CD8927E60120FA8D01F01D03E5828"
    "1FEA9A1ABE97631C828E41815F34FDCDF787419FE13A3137649AA93D2584230DF5F24B5C00"
    "C88B7D7DE4367693428C730376F218A53E853B0851BAB7C53C15DA7839CBE1285DB63F6FA4"
    "5C1BB59FE1C5BB918F0F8459D7EF60ACFF5C0FA0F3FCAD1C5F4CE4416D4F4B36B05CDCEBE4"
    "FB879E95847EFBC6449CD190248843BC7EDB145FBFC4EDBB1A3C959298F08F3BA2CFBE231B"
    "BE204BE6F906209D28BD4820AB3E7BE96C26AE8A809ADD8D1A5A0B008E9570FA4C4697E116"
    "B8119892C604293683DF582B\n"
    "20120821053137 2 6 100 3071 5 DFAA35D35531E0F524F0099877A482D2AC8D589F3743"
    "94A262A8E81A8A4FB2F65FADBAB395E05D147B29D486DFAA41F41597A256DA82A8B6F76401"
    "AED53D0253F956CEC610D417E42E3B287F7938FC24D8821B40BFA218A956EB7401BED6C96C"
    "68C7FD64F8170A8A76B953DD2F05420118F6B144D8FE48060A2BCB85056B478EDEF96DBC70"
    "427053ECD2958C074169E9550DD877779A3CF17C5AC850598C7586BEEA9DCFE9DD2A5FB62D"
    "F5F33EA7BC00CDA31B9D2DD721F979EA85B6E63F0C4E30BDDCD3A335522F9004C4ED50B15D"
    "C537F55324DD4FA119FB3F101467C6D7E1699DE4B3E3C478A8679B8EB3FA5C9B826B44530F"
    "D3BE9AD3063B240B0C853EBDDBD68DD940332D98F148D5D9E1DC977D60A0D23D0CA1198637"
    "FEAE4E7FAAC173AF2B84313A666CFB4EE6972811921D0AD867CE57F3BBC8D6CB057E3B6675"
    "7BB46C9F72662624D44E14528327E3A7100E81A12C43C4E236118318CD90C8AA185BBB0C76"
    "4826DAEAEE8DD245C5B451B4944E6122CC522D1C335C2EEF942284EA9F\n";

const char modulus_2048[] =
    "DD2047CBDBB6F8E919BC63DE885B34D0FD6E3DB2887D"
    "8B46FE249886ACED6B46DFCD5553168185FD376122171CD8927E60120FA8D01F01D03E5828"
    "1FEA9A1ABE97631C828E41815F34FDCDF787419FE13A3137649AA93D2584230DF5F24B5C00"
    "C88B7D7DE4367693428C730376F218A53E853B0851BAB7C53C15DA7839CBE1285DB63F6FA4"
    "5C1BB59FE1C5BB918F0F8459D7EF60ACFF5C0FA0F3FCAD1C5F4CE4416D4F4B36B05CDCEBE4"
    "FB879E95847EFBC6449CD190248843BC7EDB145FBFC4EDBB1A3C959298F08F3BA2CFBE231B"
    "BE204BE6F906209D28BD4820AB3E7BE96C26AE8A809ADD8D1A5A0B008E9570FA4C4697E116"
    "B8119892C604293683DF582B";

/* test if the best dhgroup size is chosen out of lists */
static void torture_dhgroup_better_size(UNUSED_PARAM(void **state))
{
    /* series of group sizes, as they are read in the file, along with expected
     * value at every moment. */
    size_t groups[][5][2] = {
        {{1024,1024}, {2048, 1024}, {1500, 1024}, {1023,1024}, {512, 1024}},
        {{512, 512}, {1023, 1023}, {1025, 1025}, {1500, 1025}, {2000, 1025}},
        {{512, 512}, {2049, 512}, {768, 768}, {4096, 768}, {1024, 1024}}
    };
    size_t i, j, best;

    for (i = 0; i < 3; ++i) {
        best = 0;
        for (j = 0; j < 5; ++j) {
            bool ok;

            ok = dhgroup_better_size(512, 1024, 2048, best, groups[i][j][0]);
            if (ok) {
                best = groups[i][j][0];
                assert_int_equal(best, groups[i][j][1]);
            }
            assert_int_equal(best, groups[i][j][1]);
        }
    }
}

static void torture_retrieve_dhgroup_file(UNUSED_PARAM(void **state))
{
    FILE *moduli = tmpfile();
    size_t size = 0;
    char *generator = NULL, *modulus = NULL;
    int rc;

    fwrite(moduli_content, 1, sizeof(moduli_content), moduli);
    rewind(moduli);
    rc = ssh_retrieve_dhgroup_file(moduli,
                                   1024,
                                   2048,
                                   4096,
                                   &size,
                                   &generator,
                                   &modulus);
    assert_int_equal(rc, SSH_OK);
    assert_int_equal(size, 2048);
    assert_string_equal(modulus, modulus_2048);

    SAFE_FREE(generator);
    SAFE_FREE(modulus);
    fclose(moduli);
}

int torture_run_tests(void) {
    int rc;
    struct CMUnitTest tests[] = {
        cmocka_unit_test(torture_dhgroup_better_size),
        cmocka_unit_test(torture_retrieve_dhgroup_file)
    };

    ssh_init();
    torture_filter_tests(tests);
    rc = cmocka_run_group_tests(tests, NULL, NULL);
    ssh_finalize();
    return rc;
}
