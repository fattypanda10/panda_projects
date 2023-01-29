""" Parser Test """
import pytest


@pytest.mark.parametrize(
    "unsorted_dict,sorted_dict_desc,sorted_dict_asc",
    [
        (
            {"a": 1, "b": 5, "c": 3},
            [("b", 5), ("c", 3), ("a", 1)],
            [("a", 1), ("c", 3), ("b", 5)],
        )
    ],
)
def test_parser_sort_dict_len_value(
    parser_without_contents, unsorted_dict, sorted_dict_desc, sorted_dict_asc
):
    assert isinstance(parser_without_contents.sort_dict_len(unsorted_dict), list)
    assert parser_without_contents.sort_dict_len(unsorted_dict) == sorted_dict_asc
    assert (
        parser_without_contents.sort_dict_len(
            unsorted_dict,
            desc=True,
        )
        == sorted_dict_desc
    )


def test_parser_byte_to_str(parser_without_contents, parser_byte_to_str):
    assert isinstance(parser_without_contents.convert_to_str(parser_byte_to_str), str)


def test_parser_process_data(parser_without_contents, parser_process_data):
    parser_without_contents._process_contents(parser_process_data)
    processed_dict = parser_without_contents.package_file_dict_len
    assert "ungrouped_data" in processed_dict
    assert processed_dict["ungrouped_data"] == 2
    assert processed_dict == {
        "p1": 1,
        "p2": 2,
        "p3": 3,
        "p4": 0,
        "p5": 4,
        "ungrouped_data": 2,
    }


def test_contents_dict_empty(parser_without_contents, parser_process_data):
    parser_without_contents._process_contents(parser_process_data)
    assert not parser_without_contents.package_file_dict


def test_contents_dict_not_empty(parser_with_contents, parser_process_data):
    parser_with_contents._process_contents(parser_process_data)
    assert parser_with_contents.package_file_dict
